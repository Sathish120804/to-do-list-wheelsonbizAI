import {
  HashRouter,
  Routes,
  Route,
} from "react-router-dom";

import Signup from "./pages/Signup";
import Signin from "./pages/Signin";
import Dashboard from "./pages/Dashboard";

function App() {
  return (
    <HashRouter>
      <Routes>

        <Route
          path="/"
          element={<Signin />}
        />

        <Route
          path="/signup"
          element={<Signup />}
        />

        <Route
          path="/dashboard"
          element={<Dashboard />}
        />

      </Routes>
    </HashRouter>
  );
}

export default App;