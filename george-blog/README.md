# Gatsby a static Progressive Web Apps Generator

This folder is create by command `gatsby new <project name>`. and install the a couple more dependencies like `gatsby-source-filesystem` and `gatsby-transformer-remark`. `gatsby-source-filesystem` create **File** nodes from the file system, whereas `gatsby-transformer-remark` will transform any `Markdown(.md)` files into **MarkdownRemark** nodes, making it easier to query them.

`gatsby-config.js` file is a webpack configure liking file.

# Setup your site

## Set index blog
Go to `src/pages` folder and create a directory name as `My Blogs #1` to store you `markdown` files. And create a `index.md` write like:
```bash
---
path: '/my-blog-path'
date: '2018-05-23T12:34:00+00:00'
title: "My first Blog"
tags: ['The Flash', "Batman", "Superman", "Wally West", "Wonder Woman", "DC"]
excerpt: "It all begins here. Do not skip to the last page. Do not let a friend or message board ruin this comic for you. The future (and past) of the DC Universe starts here. Don’t say I didn’t warn you!"
---
(Start writing your blog post from here)
```
Here `path` is the URL to access this post. `date` using **Unix TimeStamp**, `title` for the blog post, `tag` is a list of key words be able to search for the post, `excerpt` is a small summary that it will show on the main Blog's page.

## Create an index of your posts

Go to `src/pages/index.js` write the following code:
```js
import React from 'react';
import Link from 'gatsby-link';

const IndexPage = ({data}) => {
  const {edges: posts} = data.allMarkdownRemark;
  return (
    <div>
      {posts.map (({node: post}) => {
        const {frontmatter} = post;
        return (
          <div>
            <h2>
              <Link to={frontmatter.path}>
                {frontmatter.title}
              </Link>
            </h2>
            <p>{frontmatter.date}</p>
            <p>{frontmatter.excerpt}</p>
          </div>
        );
      })}
    </div>
  );
};

export const query = graphql`
  query IndexQuery {
    allMarkdownRemark {
      totalCount
      edges {
        node {
          id
          frontmatter {
            title
            date(formatString: "MMMM DD, YYYY")
            path
            tags
            excerpt
          }
        }
      }
    }
  }
`;

export default IndexPage;
```
Here is take a look of the GraphQL query, which is going to take in all the Markdown files inside the `src` folder. It will then give out the total number of markdown files (totalCount) and set up `edges` containing `node`. The `edge` is a file system path to the `node`.Here `node` is nothing but our `blog` post. Finally this data is then taken into the `indexpage` component.

Then you can run the command of `npm run develop` to start the web site.

# Building a Template for the Blog Post

Pass the blog post's data into a template component built using React. A `src` directory, create a new folder called `templates`. Create a template component inside this folder and name the file as `blog-post.js`.