import { useEffect, useState } from "react"
import { useParams, Link } from "react-router-dom"

function BlogDetail() {

  const { id } = useParams()

  const [blog, setBlog] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState("")

  useEffect(() => {

    fetch(`http://127.0.0.1:8000/api/blogs/${id}/`)
      .then((response) => {

        if (!response.ok) {
          throw new Error("Blog not found")
        }

        return response.json()
      })
      .then((data) => {

        setBlog(data)
        setLoading(false)

      })
      .catch((error) => {

        console.error(error)

        setError(error.message)
        setLoading(false)

      })

  }, [id])

  if (loading) {
    return <p>Loading blog...</p>
  }

  if (error) {
    return <p>{error}</p>
  }

  return (
    <div>

      <Link to="/">
        ← Back to Blogs
      </Link>

      <h1>{blog.title}</h1>

      <p>
        Author: {blog.author}
      </p>

      <p>
        Views: {blog.number_of_views}
      </p>

      <p>
        Published: {blog.isPublished ? "Yes" : "No"}
      </p>

      <hr />

      <p>
        {blog.content}
      </p>

    </div>
  )
}

export default BlogDetail