# FastAPI with Flagsmith Integration

This repository demonstrates an example of integrating Flagsmith with FastAPI for feature flag management within your API. Flagsmith allows teams to control feature flags and configurations, facilitating feature rollouts, experiments, and A/B testing with ease.

## Overview

Integrating FastAPI with Flagsmith provides a powerful way to manage feature access and configurations dynamically. This setup enables you to toggle features, run experiments, and roll out updates without needing to redeploy your application.

## Getting Started

To get this application running locally, follow the steps below:

### Prerequisites

Ensure you have Python 3.7+ installed on your machine. You can check your Python version by running:

```bash
python --version
```

### Installation

Clone the repository:

```bash
git clone https://github.com/bilannnn/flagsmith_ff_medium.git
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

Run the FastAPI application:

```bash
uvicorn --factory "src.ff_demo_service.asgi:build_app" 
```

Open your browser and navigate to [http://127.0.0.1:8000/api/ff-demo-service/docs/swagger/](http://127.0.0.1:8000/api/ff-demo-service/docs/swagger/)