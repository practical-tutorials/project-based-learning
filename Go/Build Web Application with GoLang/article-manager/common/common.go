package common

import (
	"net/http"
	"net/http/httptest"
	"os"
	"testing"

	"github.com/gin-gonic/gin"
)

// TestMain is used for setup before executing the test functions
func TestMain(m *testing.M) {
	// Set Gin to Test Mode
	gin.SetMode(gin.TestMode)

	// Run the other tests
	os.Exit(m.Run())
}

// TestHTTPResp is a helper function to process a request and test its response
func TestHTTPResp(t *testing.T, r *gin.Engine, req *http.Request, f func(rr *httptest.ResponseRecorder) bool) {
	// Create a response recorder
	recorder := httptest.NewRecorder()

	// Create the service and process the above request.
	r.ServeHTTP(recorder, req)

	if !f(recorder) {
		t.Fail()
	}
}

// GetRouter is a helper function to create a router during testing
func GetRouter(withTemplates bool) *gin.Engine {
	r := gin.Default()
	if withTemplates {
		r.LoadHTMLGlob("template/*")
	}

	return r
}

// Render renders one of HTML, JSON or CSV based on the 'Accept' header of the request
// If the header doesn't specify this, HTML is rendered, provided that
// the template name is present
func Render(c *gin.Context, data gin.H, templateName string) {

	switch c.Request.Header.Get("Accept") {
	case "application/json":
		// Respond with JSON
		c.JSON(http.StatusOK, data["payload"])
	case "application/xml":
		// Respond with XML
		c.XML(http.StatusOK, data["payload"])
	default:
		// Respond with HTML
		c.HTML(http.StatusOK, templateName, data)
	}

}
