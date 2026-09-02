import { Link } from "react-router-dom"

function BlogCard({ blog }) {

  return (
    <article className="blog-card">

      <h2>
        <Link to={`/blogs/${blog.id}/`}>
          {blog.title}
        </Link>
      </h2>

      <p>
        {blog.content}
      </p>

      <p>
        Author: {blog.author}
      </p>

      <p>
        Views: {blog.number_of_views}
      </p>

    </article>
  )
}

export default BlogCard