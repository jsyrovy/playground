namespace InMemoryDb
{
    public class BloggingService
    {
        private readonly BloggingContext bloggingContext;

        public BloggingService(BloggingContext bloggingContext)
        {
            this.bloggingContext = bloggingContext;
        }

        public void Add(object entity)
        {
            this.bloggingContext.Add(entity);
            this.bloggingContext.SaveChanges();
        }
    }
}
