<template>
  <div>
    <div class="article-frame">
      <div class="title">
        <div>
          <h3
            style="
              font-family: 'Jeju Gothic', sans-serif !important;
              color: rgb(27, 45, 71);
              font-size: 28px;
            "
          >
            {{ article.title }}
          </h3>
        </div>
        <div>
          <v-menu bottom left :disabled="!isAuthor">
            <template v-slot:activator="{ on, attrs }">
              <v-btn icon v-bind="attrs" v-on="on">
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item>
                <v-list-item-title
                  @click="
                    $router.push({
                      name: 'articleEdit',
                      params: { articlePk: articlePk },
                    })
                  "
                  style="cursor: pointer"
                >
                  게시글 수정
                </v-list-item-title>
              </v-list-item>
              <v-list-item>
                <v-list-item-title @click="deleteArticle(article.pk)" style="cursor: pointer">
                  게시글 삭제
                </v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </div>
      </div>
      <!-- 부제목, username과 좋아요, 댓글버튼 들어감 -->
      <div class="subtitle">
        <div style="display: flex; align-items: center">
          <div class="subtitle-item">
            <v-avatar
              color="primary"
              size="56"
              style="font-family: 'Jeju Gothic', sans-serif !important"
            >
              <img :src="profile.profile_img" alt="프로필"
            /></v-avatar>
          </div>
          <div style="margin-left: 10px">
            <h4 style="font-family: 'Jeju Gothic', sans-serif !important">
              <router-link
                :to="{
                  name: 'profileCommunity',
                  params: { username: $route.params.user.username },
                }"
                class="router__author"
                >{{ $route.params.user.username }}</router-link
              >
            </h4>
          </div>
        </div>
        <div style="display: flex; align-items: center">
          <!-- 좋아요 -->
          <div class="subtitle-item">
            <v-btn
              icon
              :color="liked ? 'red darken-2' : 'grey'"
              @click="
                likeArticle(articlePk);
                liked = !liked;
              "
            >
              <v-icon>mdi-heart</v-icon>
            </v-btn>
          </div>
          <!-- 댓글 -->

          <v-row justify="center">
            <v-dialog v-model="dialog" persistent max-width="600px">
              <template v-slot:activator="{ on, attrs }">
                <div class="subtitle-item">
                  <v-btn color="blue darken-4" icon v-bind="attrs" v-on="on">
                    <v-icon>mdi-message-text</v-icon>
                  </v-btn>
                </div>
              </template>

              <v-card>
                <v-card-title>
                  <span class="comment-title">댓글 작성하기</span>
                </v-card-title>
                <div class="textarea">
                  <v-textarea v-model="content" color="amber darken-4">
                    <template v-slot:label>
                      <div>댓글 내용을 작성해주세요 <small></small></div>
                    </template>
                  </v-textarea>
                </div>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="dialog = false">
                    닫기
                  </v-btn>
                  <v-btn
                    color="blue darken-1"
                    text
                    @click="
                      dialog = false;
                      createComment({ articlePk, content });
                      content = '';
                    "
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
      <div
        class="content"
        style="
          font-family: 'Jeju Gothic', sans-serif !important;
          font-size: 20px;
        "
      >
        {{ article.content }}
      </div>
      <!-- 댓글 -->
      <div class="comments">
        <div v-for="comment in article.comments" :key="comment.pk">
          <comment-view
            :comment="comment"
            :articlePk="articlePk"
            :username="$route.params.username"
          ></comment-view>
        </div>
      </div>
    </div>
    <div style="display: flex; justify-content: center">
      <v-btn
        rounded
        class="ma-2"
        color="blue darken-4"
        large
        dark
        @click="$router.push({ name: 'community' })"
      >
        <v-icon dark left> mdi-arrow-left </v-icon>뒤로가기
      </v-btn>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import CommentView from "../components/CommentView.vue";

export default {
  name: "ArticleDetailView",
  data() {
    return {
      content: "",
      articlePk: this.$route.params.articlePk,
      dialog: false,
      liked: this.$route.params.isLiked,
      articleComments: this.$route.params.articleComments,
      user: JSON.parse(localStorage.getItem("currentUser")),
    };
  },
  components: {
    CommentView,
  },
  methods: {
    ...mapActions([
      "toggleCommentLiked",
      "fetchArticle",
      "likeArticle",
      "deleteArticle",
      "createComment",
      "fetchProfile",
    ]),
  },
  computed: {
    ...mapGetters(["isAuthor", "isCommentLiked", "article", "profile"]),
  },
  async created() {
    await this.fetchArticle(this.articlePk);

    const payload = { username: this.$route.params.username };
    this.fetchProfile(payload);
  },
};
</script>

<style>
.article-frame {
  font-family: "Jeju Gothic", sans-serif !important;
  margin: 50px auto 10px;
  width: 900px;
  border: 2px solid rgb(40, 129, 221);
  border-radius: 5px;
}
.title {
  font-family: "Jeju Gothic", sans-serif !important;
  display: flex;
  margin-bottom: 30px;
  padding-top: 10px;
  padding-left: 20px;
  padding-right: 10px;
  justify-content: space-between;
  font-size: 24px;
}
.subtitle {
  font-family: "Jeju Gothic", sans-serif !important;
  width: 90%;
  margin: 0 auto 20px;
  font-size: small;
  display: flex;
  justify-content: space-between;
  padding: 5px 5px 15px;
  border-bottom: 3px solid rgb(165, 165, 187);
}
.subtitle-item {
  font-family: "Jeju Gothic", sans-serif !important;
  margin: 0 5px;
}
.article-frame .subtitle .subtitle-item {
  font-family: "Jeju Gothic", sans-serif !important;
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
  font-family: "Jeju Gothic", sans-serif !important;
  font-weight: bold !important;
  color: rgb(2, 7, 21);
  font-size: 24px;
}

.router__author {
  color: rgb(2, 7, 21) !important;
  font-weight: bold;
}
</style>
