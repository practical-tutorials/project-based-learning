package model

import (
	"testing"
)

func TestGetAllArticles(t *testing.T) {
	alist := GetAllArticles()

	if len(alist) != len(articleList) {
		t.Fail()
	}

	for i, v := range alist {
		if v.ID != articleList[i].ID ||
			v.Title != articleList[i].Title ||
			v.Content != articleList[i].Content {

			t.Fail()
			break
		}
	}
}

func TestGetArticleByID(t *testing.T) {
	a, err := GetArticleByID(1)

	if err != nil ||
		a.ID != 1 {
		t.Fail()
	}
}
