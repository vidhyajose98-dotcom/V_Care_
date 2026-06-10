Deployment Runbook: Vercel Frontend + Render Backend (Monorepo)

Overview
- Frontend is deployed to Vercel from the monorepo at frontend/vcare.
- Backend is deployed to Render from the monorepo at backend/.
- The two apps communicate via an API base URL configured in the frontend (VITE_API_BASE_URL or REACT_APP_API_BASE_URL).
- The GitHub repo used: https://github.com/vidhyajose98-dotcom/V_Care_/ 

Prerequisites
- GitHub repository access with admins rights to install GitHub Actions/Integrations if used.
- Render account connected to the repository (via GitHub integration).
- Vercel account connected to the repository (via GitHub integration).
- Backend credentials securely stored in Render Secrets (Supabase, database URL, etc.). Do not store sensitive values in code.

1) Configure environment variables (placeholders; replace with actual values when deploying)
- FRONTEND_URL: the final Vercel frontend URL (e.g., https://your-app.vercel.app) [optional for CORS in backend; you can also set FRONTEND_URL after frontend deployment]
- VITE_API_BASE_URL: the base URL for the backend API, typically the Render URL (e.g., https://your-backend.onrender.com). If using Render, set in the frontend environment as VITE_API_BASE_URL
- BACKEND_SUPABASE_URL, BACKEND_SUPABASE_ANON_KEY, DATABASE_URL: stored in Render Secrets, not in code
- Any other secrets required by backend (e.g., third-party API keys) stored in Render Secrets

2) Render: Deploy backend
- In the Render dashboard, create a new Web Service
  - Root Directory: backend
  - Use backend/render.yaml for configuration
  - Build Command: pip install -r requirements.txt
  - Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
  - Environment: Use Python selector compatible with your code (e.g., Python 3.11)
  - Secrets: Add all required secrets (e.g., SUPABASE_URL, SUPABASE_ANON_KEY, DATABASE_URL) accessible to backend via environment variables
- Deploy and note the backend URL (e.g., https://vcare-backend.onrender.com)

3) Vercel: Deploy frontend
- In Vercel, create/import a project from the same GitHub repo
  - Root Directory: frontend/vcare (or rely on vercel.json at repo root with rootDirectory set)
  - Ensure the project uses the monorepo configuration (vercel.json)
  - Environment: Set VITE_API_BASE_URL to the Render backend URL or rely on an environment variable in vercel.json if preferred
- Deploy and note the frontend URL (e.g., https://vcare-app.vercel.app)

4) Wire and test
- In the backend, ensure allowed_origins includes the frontend URL after deployment (via FRONTEND_URL or by whitelisting the Vercel domain)
- In the frontend, update any API calls to use the API base URL from environment variable (import.meta.env.VITE_API_BASE_URL or process.env.REACT_APP_API_BASE_URL depending on setup)
- Open the frontend URL and verify the app loads; trigger a simple API call to backend health endpoints

5) Verification checklist
- [ ] Backend deployed to Render and reachable at its URL
- [ ] Frontend deployed to Vercel and reachable at its URL
- [ ] Frontend successfully calls backend endpoints (health or sample API)
- [ ] Documentation updated with runbook and URLs

Notes
- Do not expose credentials in code or public repos.
- If you need rollback, revert the latest deployment in Vercel/Render or revert the GitHub commit.

End of runbook

CI/CD Kickoff
- To trigger Render + Vercel deployments, push a small non-sensitive change to the repo (e.g., update RUNBOOK.md with a timestamp) to trigger the GitHub Actions workflow.
- Monitor the GitHub Actions tab for Deploy Monorepo to Render & Vercel (Monorepo) and wait for completion.
- After completion, retrieve the deployed URLs from the Render dashboard (backend) and Vercel dashboard (frontend) or from the CI run logs.
- Deployed URLs (latest CI run)
  - Latest CI run: https://github.com/vidhyajose98-dotcom/V_Care_/actions/runs/27294315950
  - Backend (Render) URL: [to be filled after deployment]
  - Frontend (Vercel) URL: [to be filled after deployment]
- How to fetch deployed URLs now:
  - Run: python fetch_github_run_url.py
  - Then check the Render/Vercel dashboards for the finalized URLs if not present in CI logs.

- Quick runbook addition for reproducibility
  - Ensure repository is linked to Render and Vercel via GitHub integrations.
  - Push to main to trigger the Deploy Monorepo workflow.
  - After CI completes, gather the final URLs from dashboards and update RUNBOOK.md.

CI/CD Kickoff
- To trigger the Render + Vercel deployments, push a small non-sensitive change to the repo (e.g., update RUNBOOK.md with a timestamp) to trigger the GitHub Actions workflow.
- Monitor the GitHub Actions tab for the job named "Deploy Monorepo to Render & Vercel (Monorepo)" and wait for completion.
- After the workflow completes, retrieve the deployed URLs from Render (backend) and Vercel (frontend) in their respective dashboards or from the GitHub Actions logs if you configured outputs.
- If the deployment fails, check logs in the Actions tab, verify secrets (Render Secrets, Vercel env vars), and ensure the monorepo structure (frontend/vcare and backend) matches the workflow expectations.
- Deployment Trigger: Updated RUNBOOK.md at $(date) to kickoff CI/CD.
- To trigger the Render + Vercel deployments, push a small non-sensitive change to the repo (e.g., update RUNBOOK.md with a timestamp) to trigger the GitHub Actions workflow.
- Monitor the GitHub Actions tab for the job named "Deploy Monorepo to Render & Vercel (Monorepo)" and wait for completion.
- After the workflow completes, retrieve the deployed URLs from Render (backend) and Vercel (frontend) in their respective dashboards or from the GitHub Actions logs if you configured outputs.
- If the deployment fails, check logs in the Actions tab, verify secrets (Render Secrets, Vercel env vars), and ensure the monorepo structure (frontend/vcare and backend) matches the workflow expectations.

- Deployed URLs (latest CI run)
  - Latest CI run URL: https://github.com/vidhyajose98-dotcom/V_Care_/actions/runs/27294315950
  - Backend (Render) URL: [to be filled after deployment]
  - Frontend (Vercel) URL: [to be filled after deployment]

- How to fetch deployed URLs now:
  - Run the helper script to fetch the latest run URL:
    - python fetch_github_run_url.py
  - Then open the CI run page in the browser and locate the deployment steps for Render and Vercel to copy the final URLs from their dashboards if not printed in logs.

- Quick runbook addition for reproducibility
  - Ensure repository is linked to Render and Vercel via GitHub integrations.
  - Push to main to trigger the Deploy Monorepo workflow.
  - After CI completes, gather the final URLs from the dashboards and update RUNBOOK.md.
