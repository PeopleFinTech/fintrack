import Home from "../pages/home"
import Login from "../pages/auth/login"
import Register from "../pages/auth/register"
import Dashboard from "../pages/dashboard"

const webRoutes = [
  {
    path: "/",
    element: <Home/>,
  },
  {
    path: "/login",
    element: <Login/>,
  },
  {
    path: "/register",
    element: <Register/>,
  },
  {
    path: "/dashboard",
    element: <Dashboard/>,
  },
]
export default webRoutes