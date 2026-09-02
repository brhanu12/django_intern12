import { useEffect, useState } from "react"

import { Link } from "react-router-dom"
import BlogList from "../components/BlogList"

function Home() {

  const [blogs, setBlogs] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState("")

  useEffect(() => {

    fetch("http://127.0.0.1:8000/api/blogs/")
      .then((response) => {

        if (!response.ok) {
          throw new Error("Failed to fetch blogs")
        }

        return response.json()
      })
      .then((data) => {

        setBlogs(data)
        setLoading(false)

      })
      .catch((error) => {

        console.error(error)

        setError(error.message)
        setLoading(false)

      })

  }, [])

  return (
    <div>

      <h1>My Django Blog</h1>
      <Link to="/create-blog/">
  Create New Blog
</Link>

      {loading && (
        <p>Loading blogs...</p>
      )}

      {error && (
        <p>{error}</p>
      )}

      {!loading && !error && (
        <BlogList blogs={blogs} />
      )}

    </div>
  )
}

export default Home