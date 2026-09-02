import { useState } from "react"
import { useNavigate } from "react-router-dom"

function CreateBlog() {
  const navigate = useNavigate()

  const [title, setTitle] = useState("")
  const [content, setContent] = useState("")
  const [isPublished, setIsPublished] = useState(false)

  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")
  const [success, setSuccess] = useState("")

  function handleSubmit(event) {
    event.preventDefault()

    setLoading(true)
    setError("")
    setSuccess("")

    const accessToken = localStorage.getItem("access_token")

    console.log("TOKEN EXISTS:", !!accessToken)

    if (!accessToken) {
      setError("You are not logged in. Access token was not found.")
      setLoading(false)
      return
    }

    const blogData = {
      title: title,
      content: content,
      isPublished: isPublished,
    }

    console.log("SENDING DATA:", blogData)

    fetch("http://127.0.0.1:8000/api/blogs/", {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${accessToken}`,
      },

      body: JSON.stringify(blogData),
    })
      .then(async (response) => {
        console.log("STATUS:", response.status)

        const text = await response.text()

        console.log("DJANGO RESPONSE:", text)

        let data

        try {
          data = JSON.parse(text)
        } catch {
          data = { detail: text }
        }

        if (!response.ok) {
          throw new Error(
            data.detail ||
            data.error ||
            JSON.stringify(data)
          )
        }

        return data
      })

      .then((data) => {
        console.log("CREATED BLOG:", data)

        setSuccess("Blog created successfully!")

        setTitle("")
        setContent("")
        setIsPublished(false)

        setTimeout(() => {
          navigate(`/blogs/${data.id}/`)
        }, 1000)
      })

      .catch((error) => {
        console.error("CREATE BLOG ERROR:", error)

        setError(error.message)
      })

      .finally(() => {
        setLoading(false)
      })
  }

  return (
    <div
      style={{
        maxWidth: "700px",
        margin: "40px auto",
        padding: "30px",
      }}
    >

      <h1>Create Blog</h1>

      {error && (
        <div
          style={{
            color: "red",
            backgroundColor: "#ffe6e6",
            padding: "12px",
            marginBottom: "20px",
            borderRadius: "6px",
          }}
        >
          <strong>Error:</strong> {error}
        </div>
      )}

      {success && (
        <div
          style={{
            color: "green",
            backgroundColor: "#e6ffe6",
            padding: "12px",
            marginBottom: "20px",
            borderRadius: "6px",
          }}
        >
          {success}
        </div>
      )}

      <form onSubmit={handleSubmit}>

        <div style={{ marginBottom: "20px" }}>
          <label
            htmlFor="title"
            style={{
              display: "block",
              marginBottom: "8px",
              fontWeight: "bold",
            }}
          >
            Blog Title
          </label>

          <input
            id="title"
            type="text"
            value={title}
            onChange={(event) => setTitle(event.target.value)}
            placeholder="Enter blog title"
            required
            style={{
              width: "100%",
              padding: "10px",
              boxSizing: "border-box",
            }}
          />
        </div>

        <div style={{ marginBottom: "20px" }}>
          <label
            htmlFor="content"
            style={{
              display: "block",
              marginBottom: "8px",
              fontWeight: "bold",
            }}
          >
            Blog Content
          </label>

          <textarea
            id="content"
            value={content}
            onChange={(event) => setContent(event.target.value)}
            placeholder="Write your blog..."
            rows="10"
            required
            style={{
              width: "100%",
              padding: "10px",
              boxSizing: "border-box",
              resize: "vertical",
            }}
          />
        </div>

        <div style={{ marginBottom: "20px" }}>
          <label>
            <input
              type="checkbox"
              checked={isPublished}
              onChange={(event) =>
                setIsPublished(event.target.checked)
              }
            />

            {" "}Publish this blog
          </label>
        </div>

        <button
          type="submit"
          disabled={loading}
          style={{
            padding: "12px 25px",
            cursor: loading ? "not-allowed" : "pointer",
          }}
        >
          {loading ? "Creating..." : "Create Blog"}
        </button>

      </form>

    </div>
  )
}

export default CreateBlog