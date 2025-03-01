# NeuroGuard

NeuroGuard leverages machine learning to predict stroke risk based on user-provided health data. The application collects input, transmits it to the server, processes it using a trained model, and displays the result.

## Beta Version
[NeuroGuard Beta](https://neuro-guard.vercel.app/) *(Under Development)*  

## Backend Info
- **Backend:** Flask REST API hosted on Render.  
- **Note:** The server may take a few seconds to respond initially. This is normal and only affects the first request; subsequent requests will load faster.
- **Functionality:** Receives user data as POST requests, processes it through a machine learning model, and returns stroke risk predictions as JSON responses.
