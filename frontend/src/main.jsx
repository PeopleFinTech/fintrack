import * as React from "react";
import * as ReactDOM from "react-dom";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import './index.css'
import webRoutes from "./app/routes";
import { store } from "./redux";
import { Provider } from "react-redux";

const router = createBrowserRouter(
  webRoutes
);
// As of React 18
const root = ReactDOM.createRoot(document.getElementById('root'))


root.render(
    <Provider store={store}>
      <React.StrictMode>
          <RouterProvider router={router} />
      </React.StrictMode>
    </Provider>
);
