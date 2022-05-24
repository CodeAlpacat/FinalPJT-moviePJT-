import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

const VIDEO_API = '/videos?api_key='
const API_KEY = 'c0ea5b6535679915d16aada2f7427157'
const BASE_URL = 'https://api.themoviedb.org/3/movie/'
const VIDEO_URL = 'https://www.youtube.com/embed/'

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
    follow: {},
    followMovies: {},
    profileEdit: {},
    movieTrailer: null,
    nowUserProfile: {},
  },
  // 모든 state는 getters 를 통해서 접근하겠다.
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
    dialogDetail: state => state.dialogDetail,
    movie: state => state.movie,
    follow: state => state.follow,
    followMovies: state => state.followMovies,
    currentReview: state => state.currentReview,
    profileEdit: state => state.profileEdit,
    videoUrl: state => VIDEO_URL + state.movieTrailer,
    isVideo: state => (state.movieTrailer != null),
    nowUserProfile: state => state.nowUserProfile,
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_NOW_USER_PROFILE: (state, nowUserProfile) => state.nowUserProfile = nowUserProfile,
    SET_EDIT_PROFILE: (state, profileEdit) => state.profileEdit = profileEdit,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SET_DIALOG_DETAIL: (state) => state.dialogDetail = !state.dialogDetail,
    SET_DIALOG_COMMENT : (state) => state.dialogComment = !state.dialogComment,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_CURRENT_REVIEW: (state, review) => state.review = review,
    SET_COMMENT_LIKED: (state) => state.commentLiked = !state.commentLiked, // comment_liked의 경우 시험용으로 comment 좋아요 정보를 받아오고 있지 않음, 추후 추가할것
    SET_FOLLOW: (state, follow) => state.follow = follow,
    SET_FOLLOW_MOVIES: (state, followMovies) => state.followMovies = followMovies,
    SET_MOVIE_REVIEWS: (state, reviews) => (state.movie.reviews = reviews),
    SET_MOVIE_TRAILER: (state, video) => (state.movieTrailer = video),
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

      axios({
        url: drf.accounts.profile(username),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_PROFILE', res.data)
        })
        .catch(err => console.log(err.response))
    },

    fetchNowUserProfile({ commit, getters }, { username }) {

      axios({
        url: drf.accounts.profile(username),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_NOW_USER_PROFILE', res.data)
        })
        .catch(err => console.log(err.response))
    },

    movieSelect({commit}, movie){
      commit('SET_MOVIE', movie)
    },

    followProfile({ commit, getters }, userPk) {
      
      axios({
        url: drf.accounts.follow(userPk),
        method: 'post',
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_FOLLOW', res.data)
        commit('SET_NOW_USER_PROFILE', res.data)
      })
      .catch(err => console.log(err.response))
    },

    followMovies({ commit, getters }, moviePk) {
      axios({
        url: drf.accounts.followMovies(moviePk),
        method: 'post',
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_FOLLOW_MOVIES', res.data)
        commit('SET_PROFILE', res.data)
      })
      .catch(err => console.log(err.response))
    },
    
    updateProfile({ commit, getters }, { currentUsername, username, genre_likes, email, profile_img }) {
      
      axios({
        url: drf.accounts.profile(currentUsername),
        method: 'put',
        data: { username, genre_likes, email, profile_img },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_EDIT_PROFILE', res.data)
          commit('SET_PROFILE', res.data)
          router.push({
            name: 'profileCommunity',
            params: { username }
          })
        })
        .catch(err=> console.log(err.response))
    },

    createReview({ commit, getters}, { moviePk, content }) {
      const review = {content}
      axios({
        url: drf.accounts.reviews(moviePk),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    likeReview({ commit, getters}, { moviePk, reviewPk }) {
      axios({
        url: drf.accounts.likeReview(moviePk, reviewPk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    deleteReview({ commit, getters }, { moviePk, reviewPk }) {
      if (confirm('정말 댓글을 삭제하시겠습니까?')){
        axios({
          url: drf.accounts.review(moviePk, reviewPk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_MOVIE_REVIEWS', res.data)
            })
          .catch(err => console.error(err.response))
      }
    },

    getMovieTrailer({ commit }, MoviePk) {
      axios({
        url: BASE_URL + String(MoviePk) + VIDEO_API + API_KEY
      })
        .then(res => {
          commit('SET_MOVIE_TRAILER', res.data.results[0].key)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
}
