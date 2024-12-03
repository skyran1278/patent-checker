# Getting Started

To start the application, run the following commands:

```sh
echo "OPENAI_API_KEY=<your_openai_api_key>" >> backend/.env
echo "NEXT_PUBLIC_API_URL=http://backend:8000" >> frontend/.env
docker compose build
docker compose up -d
```

Once done, you can access the web app at [http://localhost:3000](http://localhost:3000).

Alternatively, the app is also hosted at [http://patent-publi-4uksrxiayttb-1083196034.ap-northeast-1.elb.amazonaws.com/](http://patent-publi-4uksrxiayttb-1083196034.ap-northeast-1.elb.amazonaws.com/).

# Technical Requirements

- ✅ Include a simple **README.md** file with instructions on how to run the application.
- ✅ The application must be **dockerized** (avoid using port 5000), so there’s no need for manual installation of development dependencies or environment setup.
- ✅ Use **Python** for the backend and **TypeScript** for the frontend. You may choose any frameworks or libraries that suit your needs.
- ✅ **Bonus Points**: Host and run the app on a **web server**.
- ✅ **Bonus Points**: Implement basic **user input parsing** to enable fuzzy matching with the given dataset.
- ⬜ **Bonus Points**: Provide users with the ability to **save results as a report** and later view previously saved reports within the app.
