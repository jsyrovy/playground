using Microsoft.EntityFrameworkCore;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Linq;

namespace InMemoryDb.UnitTests
{
    [TestClass]
    public class BloggingServiceTests
    {
        [TestMethod]
        public void Add()
        {
            var url = "http://example.com";
            var options = new DbContextOptionsBuilder<BloggingContext>().UseInMemoryDatabase("db").Options;

            using (var context = new BloggingContext(options))
            {
                var service = new BloggingService(context);
                service.Add(new Blog { Url = url });
            }

            using (var context = new BloggingContext(options))
            {
                var blogs = context.Blogs;

                Assert.AreEqual(1, blogs.Count());
                Assert.AreEqual(url, blogs.First().Url);
            }
        }
    }
}
