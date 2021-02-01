package handler

import (
	"net/http"
	"strconv"

	"github.com/c-major/article_manager/common"
	"github.com/c-major/article_manager/model"
	"github.com/gin-gonic/gin"
)

// ShowIndexPage .
func ShowIndexPage(c *gin.Context) {
	articleList := model.GetAllArticles()

	// Call the render function with the name of the template to render
	common.Render(c,
		gin.H{
			"title":   "Home Page",
			"payload": articleList,
		},
		"index.html")
}

// GetArticle .
func GetArticle(c *gin.Context) {
	// check if the article id is valid
	articleID, err := strconv.Atoi(c.Param("article_id"))
	if err != nil {
		// If an invalid article ID is specified in the URL, abort with an error
		c.AbortWithStatus(http.StatusNotFound)
	}

	// Check if the article exists
	article, err := model.GetArticleByID(articleID)
	if err != nil {
		// If the article is not found, abort with an error
		c.AbortWithError(http.StatusNotFound, err)
	}

	// Call the HTML method of the Context to render a template
	c.HTML(
		// Set the HTTP status to 200 (OK)
		http.StatusOK,
		// Use the index.html template
		"article.html",
		// Pass the data that the page uses
		gin.H{
			"title":   article.Title,
			"payload": article,
		},
	)
}
