<template>
  <v-form @submit.prevent="onSubmit">
    <div>
      <v-text-field
        label="제목을 작성해 주세요."
        :rules="titleRules"
        hide-details="auto"
         v-model="newArticle.title"
      ></v-text-field>
        <v-textarea
          background-color="indigo lighten-5"
          clearable
          clear-icon="mdi-close-circle"
          label="내용을 작성해 주세요."
          v-model="newArticle.content"
          :rules="contentRules"
        ></v-textarea>
    </div>
    <div>
      <div class="text-center">
        <v-btn
          rounded
          color="primary"
          dark
          large
          @click="onSubmit"
          style="font-family:'Jeju Gothic', sans-serif !important;"
        > {{ action==='create' ? '제출하기' : '수정하기' }}
          <v-icon
            right
            dark
          >
            mdi-pencil
          </v-icon>
        </v-btn>
        <v-btn
          rounded
          color="blue darken-4"
          dark
          large
          @click="$router.go(-1)"
          style="font-family:'Jeju Gothic', sans-serif !important; margin-left:20px;"
        > 뒤로가기
          <v-icon
            right
            dark
          >
            mdi-arrow-left
          </v-icon>
        </v-btn>
      </div>
    </div>
  </v-form>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          title: this.article.title,
          content: this.article.content,
        },
        titleRules: [
          value => !!value || '필수 항목입니다.'
        ],
        contentRules: [
          value => !!value || '필수 항목입니다.',
          value => (value && value.length >= 3) || '최소 2자 이상 적어주세요!',
        ],
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === 'create') {
          this.createArticle(this.newArticle)
        } else if (this.action === 'update') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
    },
  }
</script>

<style></style>
