import { BrowserRouter, Routes, Route } from "react-router-dom"

import Home from "./pages/Home"
import BlogDetail from "./pages/BlogDetail"
import CreateBlog from "./pages/CreateBlog"

function App() {

  return (
    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<Home />}
        />

        <Route
          path="/blogs/:id/"
          element={<BlogDetail />}
        />

        <Route
          path="/create-blog/"
          element={<CreateBlog />}
        />

      </Routes>

    </BrowserRouter>
  )
}

export default App