const HOST = 'http://localhost:8000/api/v1/'
const BASE_HOST = 'http://localhost:8000/'

const ACCOUNTS = 'accounts/'
const COMMENTS = 'comments/'
const COMMUNITY = 'community/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    // currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username +'/',
    follow: userPk => HOST + ACCOUNTS + userPk +'/' + 'follow/'
  },
  articles: {
    // /articles/
    articles: () => BASE_HOST + COMMUNITY,
    // /articles/1/
    article: articlePk => BASE_HOST + COMMUNITY + `${articlePk}/`,
    likeArticle: articlePk => BASE_HOST + COMMUNITY + `${articlePk}/` + 'like/',
    comments: articlePk => BASE_HOST + COMMUNITY + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
    BASE_HOST + COMMUNITY + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  }
}