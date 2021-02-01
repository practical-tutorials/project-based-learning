package main

import "github.com/c-major/article_manager/handler"

func initializeRoutes() {

	// Handle the index route
	router.GET("/", handler.ShowIndexPage)

	// Handle GET requests at /article/view/some_article_id
	router.GET("/article/view/:article_id", handler.GetArticle)

}
