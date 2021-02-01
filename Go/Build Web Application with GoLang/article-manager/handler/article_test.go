package handler

import (
	"io/ioutil"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"

	"github.com/c-major/article_manager/common"
	"github.com/gin-gonic/gin"
)

// Test that a GET request to the home page returns the home page with
// the HTTP code 200 for an unauthenticated user
func TestShowIndexPageUnauthenticated(t *testing.T) {
	r := gin.Default()
	r.LoadHTMLGlob("../template/*")
	r.GET("/", ShowIndexPage)

	// Create a request to send to the above route
	req, _ := http.NewRequest("GET", "/", nil)

	common.TestHTTPResp(t, r, req, func(rr *httptest.ResponseRecorder) bool {
		// Test that the http status code is 200
		statusOK := rr.Code == http.StatusOK

		// Test that the page title is "Home Page"
		// You can carry out a lot more detailed tests using libraries that can
		// parse and process HTML pages
		b, err := ioutil.ReadAll(rr.Body)
		pageOK := (err == nil && strings.Index(string(b), "<title>Home Page</title>") > 0)

		return statusOK && pageOK
	})
}

func TestGetArticleUnauthenticated(t *testing.T) {
	r := gin.Default()
	r.LoadHTMLGlob("../template/*")
	r.GET("/article/view/:article_id", GetArticle)

	// Create a request to send to the above route
	req, _ := http.NewRequest("GET", "/article/view/1", nil)

	common.TestHTTPResp(t, r, req, func(rr *httptest.ResponseRecorder) bool {
		// Test that the http status code is 200
		statusOK := rr.Code == http.StatusOK

		// Test that the page title is "Article 1"
		// You can carry out a lot more detailed tests using libraries that can
		// parse and process HTML pages
		b, err := ioutil.ReadAll(rr.Body)
		pageOK := (err == nil && strings.Index(string(b), "<title>Article 1</title>") > 0)

		return statusOK && pageOK
	})
}
