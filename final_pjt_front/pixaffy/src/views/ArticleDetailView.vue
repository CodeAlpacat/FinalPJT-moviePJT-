<template>
  <div>
    <div class="article-frame">
        <div class="title">
          <div>
            <h3>{{ article.title }}</h3>
          </div>
          <div>
            <v-menu
              bottom
              left
              :disabled="!isAuthor"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  icon
                  v-bind="attrs"
                  v-on="on"
                >
                  <v-icon>mdi-dots-vertical</v-icon>
                </v-btn>
              </template>
              <v-list>
                <v-list-item>
                  <v-list-item-title
                    @click="$router.push({ name:'articleEdit', params: {articlePk: article.pk}})"
                  >
                    게시글 수정
                  </v-list-item-title>
                </v-list-item>
                <v-list-item>
                  <v-list-item-title @click="deleteArticle(article.pk)">
                    게시글 삭제
                  </v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </div>
        </div>
      <!-- 부제목, username과 좋아요, 댓글버튼 들어감 -->
      <div class="subtitle">
        <div style="display: flex; align-items: center;">
          <div class="subtitle-item">
            <v-avatar
              color="primary"
              size="56"
            >도라</v-avatar>
          </div>
          <div style="margin-left:10px">
            <h4>{{ article.user.username }}</h4>
          </div>
        </div>
        <div style="display: flex; align-items: center;">
          <!-- 좋아요 -->
          <div class="subtitle-item">
            <v-btn
              icon
              :color="liked ? 'red darken-2' : 'grey'"
              @click="likeArticle(articlePk); liked=!liked;"
            >
              <v-icon>mdi-heart</v-icon>
            </v-btn>
          </div>
          <!-- 댓글 -->


          <v-row justify="center">
            <v-dialog
              v-model="dialog"
              persistent
              max-width="600px"
            >
              <template v-slot:activator="{ on, attrs }">
                <div class="subtitle-item">
                  <v-btn
                    color="blue darken-4"
                    icon
                    v-bind="attrs"
                    v-on="on"
                  >
                    <v-icon>mdi-message-text</v-icon>
                  </v-btn>
                </div>
              </template>

              <v-card>
                <v-card-title>
                  <span class="comment-title">댓글 작성하기</span>
                </v-card-title>
                <div class="textarea">
                <v-textarea
                  v-model="comment"
                  color="amber darken-4"
                >
                  <template v-slot:label>
                    <div>
                      댓글 내용을 작성해주세요 <small></small>
                    </div>
                  </template>
                </v-textarea>
                </div>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="blue darken-1"
                    text
                    @click="dialog=false"
                  >
                    닫기
                  </v-btn>
                  <v-btn
                    color="blue darken-1"
                    text
                    @click="dialog=false; createComment({articlePK: articlePK, content: comment})"
                  >
                    완료
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-row>

        </div>
      </div>
      <!-- 내용,  -->
      <div class="content">
        {{ article.content }}
      </div>
      <!-- 댓글 -->
      <div class="comments">
        <div v-for="comment in article.comments" :key="comment.pk">
          <comment-view :comment="comment"></comment-view>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import CommentView from '../components/CommentView.vue'

export default {
  name: 'ArticleDetailView',
  data(){ 
    return {
      comment: '',
      articlePk: this.$route.params.articlePk,
      dialog: false,
      liked: false,
    }
  },
  components:{
    CommentView,
  },
  methods: {
    ...mapActions(['toggleCommentLiked', 'fetchArticle', 'likeArticle', 'deleteArticle', 'createComment'])
  },
  computed: {
    ...mapGetters(['isAuthor', 'article'])
  },
  created() {
    this.fetchArticle(this.articlePk)
  },
}
</script>

<style>
  @import url(//fonts.googleapis.com/earlyaccess/jejogothic.css);
  .article-frame {
    font-family: 'Jeju Gothic', sans-serif;
    margin: 50px auto;
    width: 900px;
    border: 2px solid rgb(27, 45, 71)
  }
  .title {
    font-family: 'Jeju Gothic', sans-serif;
    display: flex;
    margin-bottom: 30px;
    padding-top: 10px;
    padding-left: 20px;
    padding-right: 10px;
    justify-content: space-between;
  }
  .subtitle {
    font-family: 'Jeju Gothic', sans-serif;
    width: 90%;
    margin: 0 auto 20px;
    font-size: small;
    display: flex;
    justify-content: space-between;
    padding: 5px 5px 15px;
    border-bottom: 3px solid rgb(165, 165, 187);
  }
  .subtitle-item {
    font-family: 'Jeju Gothic', sans-serif;
    margin: 0 5px;
  }
  .article-frame .subtitle .subtitle-item{
    font-family: 'Jeju Gothic', sans-serif;
    color: rgb(242, 237, 243);
  }
  .content {
    width: 90%;
    margin: 20px 5% 30px;
    padding-bottom: 20px;
    border-bottom: 2px solid rgb(165, 165, 187);
  }
  .comments {
    width: 90%;
    margin: 0 5% 20px;
  }
  
  
  .textarea {
    margin: 0 30px;
  }
  .comment-title {
    margin: 0 10px;
    font-family: 'Jeju Gothic', sans-serif !important;
    font-weight: bold !important;
    color: rgb(2, 7, 21);
    font-size: 24px;
  }
</style>