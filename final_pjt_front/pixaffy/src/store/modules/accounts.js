import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  // namespaced: true,

  // state는 직접 접근하지 않겠다!
  state: {
    token: localStorage.getItem('token') || '' ,
    currentUser: {},
    profile: {},
    authError: null,
    dialogDetail: false,  // 디테일 창 모달 토글 변수
    dialogComment: false, // 댓글 생성 모달 토글 변수
    movie: null,
    commentLiked: false, // 댓글 좋아요 여부
    articleList: [],  // 게시글 리스트
  },
  // 모든 state는 getters 를 통해서 접근하겠다.
  getters: {
    isLoggedIn: state => !!state.token,
    isCommentLiked: state => !!state.commentLiked,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
    dialogDetail: state => state.dialogDetail,
    dialogComment: state => state.dialogComment,
    movie: state => state.movie,
    articleList: state => state.articleList,
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SET_DIALOG_DETAIL: (state) => state.dialogDetail = !state.dialogDetail,
    SET_DIALOG_COMMENT : (state) => state.dialogComment = !state.dialogComment,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_COMMENT_LIKED: (state) => state.commentLiked = !state.commentLiked, // comment_liked의 경우 시험용으로 comment 좋아요 정보를 받아오고 있지 않음, 추후 추가할것
    SET_ARTICLE_LIST: (state, articleList) => state.articleList = articleList,
  },

  actions: {
    saveToken({ commit }, token) {
      /* 
      state.token 추가 
      localStorage에 token 추가
      */
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token, Date.now()+1)
    },

    removeToken({ commit }) {
      /* 
      state.token 삭제
      localStorage에 token 추가
      */
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },

    login({ commit, dispatch }, credentials) {
      /* 
      POST: 사용자 입력정보를 login URL로 보내기
        성공하면
          응답 토큰 저장
          현재 사용자 정보 받기
          메인 페이지(ArticleListView)로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'home' })
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    signup({ commit, dispatch }, formData) {
    //   /* 
    //   POST: 사용자 입력정보를 signup URL로 보내기
    //     성공하면
    //       응답 토큰 저장
    //       현재 사용자 정보 받기
    //       메인 페이지(ArticleListView)로 이동
    //     실패하면
    //       에러 메시지 표시
    //   */
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: formData,
        // headers: {'Content-Type': 'multipart/form-data'}
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'home' })
        })
        .catch(err => {
          router.push({ name: 'home' })
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    logout({ getters, dispatch }) {
      /* 
      POST: token을 logout URL로 보내기
        성공하면
          토큰 삭제
          사용자 알람
          LoginView로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        // data: {},
        headers: getters.authHeader,
      })
        .then(() => {
          dispatch('removeToken')
          alert('성공적으로 logout!')
          router.push({ name: 'login' })
        })
        .error(err => {
          console.error(err.response)
        })
    },

    fetchCurrentUser({ commit, getters, dispatch }) {
      /*
      GET: 사용자가 로그인 했다면(토큰이 있다면)
        currentUserInfo URL로 요청보내기
          성공하면
            state.cuurentUser에 저장
          실패하면(토큰이 잘못되었다면)
            기존 토큰 삭제
            LoginView로 이동
      */
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_CURRENT_USER', res.data)
            localStorage.setItem('currentUser', JSON.stringify(res.data))
          })
          .catch(err => {
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
          })
      }
    },

    fetchProfile({ commit, getters }, { username }) {
      /*
      GET: profile URL로 요청보내기
        성공하면
          state.profile에 저장
      */
      axios({
        url: drf.accounts.profile(username),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_PROFILE', res.data)
        })
    },

    toggleDialogDetail({ commit }){
      commit('SET_DIALOG_DETAIL')
    },

    toggleDialogComment({ commit }){
      commit('SET_DIALOG_COMMENT')
    },

    toggleCommentLiked({ commit }){
      commit('SET_COMMENT_LIKED')
    },

    movieSelect({commit}, movie){
      commit('SET_MOVIE', movie)
    },

    fetchArticleList({commit, getters}) {
      axios({
        url: drf.community.articleList(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          console.log('성공했니?')
          commit('SET_ARTICLE_LIST', res.data)
        })
        .catch(err => {
          console.log('실패!' + err)
        })
    }
  },
}
