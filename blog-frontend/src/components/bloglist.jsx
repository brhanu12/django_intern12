import BlogCard from "./BlogCard"

function BlogList({ blogs }) {

  return (
    <div>

      {blogs.map((blog) => (
        <BlogCard
          key={blog.id}
          blog={blog}
        />
      ))}

    </div>
  )
}

export default BlogList