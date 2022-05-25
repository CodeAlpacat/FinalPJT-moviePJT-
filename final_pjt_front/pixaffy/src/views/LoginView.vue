<template>
  <div class="login-card">
    <account-error-list v-if="authError"></account-error-list>
    <div class="login-card__div" :class="`rounded-lg`">
      <div>
        <v-img
          class="login-card__div__img"
          src="https://img.freepik.com/free-photo/white-brick-wall-texture-design-empty-white-brick-background-for-presentations_1962-1075.jpg?w=1800"
          height="450px"
          width="350px"
        >
        <v-img
            style="margin-top: 130px"
            src="https://user-images.githubusercontent.com/90893428/170347769-b6d9286e-a86b-42fd-8f52-1f5fc18fa6e8.png"
          ></v-img></v-img>
      </div>
      <!-- div와 div로 grid를 이용해 반으로 분할 -->
      <form @submit.prevent="login(credentials)" class="login-card__div__form">
        <div class="text-center my-3 login-card__div__header">
          <h1>Login</h1>
        </div>
        <div class="login-card__div__form__input">
          <v-text-field
            class="login-card__div__right"
            prepend-icon="fa-solid fa-user"
            v-model="credentials.username"
            filled
            color="blue-grey lighten-2"
            label="username"
            required
            height="10px"
          ></v-text-field>
          <div></div>
        </div>
        <div class="login-card__div__form__input">
          <v-text-field
            prepend-icon="fa-solid fa-key"
            v-model="credentials.password"
            filled
            color="blue-grey lighten-2"
            label="password"
            type="password"
            required
          ></v-text-field>
        </div>

        <!-- <v-btn rounded color="primary" dark type="button"> Rounded Button </v-btn> -->
        <button class="login-card__div__form__btn"><span>Login</span></button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import AccountErrorList from "@/components/AccountErrorList.vue";

export default {
  name: "LoginView",
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: "",
        password: "",
      },
    };
  },
  computed: {
    ...mapGetters(["authError"]),
    ...mapGetters(["isLoggedIn"]),
  },
  methods: {
    ...mapActions(["login"]),
  },
  created() {
    if (this.isLoggedIn) {
      alert("로그아웃 후 진행해주세요!");
      this.$router.back();
    }
  },
};
</script>

<style scoped>
.login-card {
  margin: 0 auto;
  margin-top: 150px;
  height: 100vh;
}

.login-card__div {
  display: grid;
  grid: auto-flow / 1fr 1fr;
  min-height: 450px;
  min-width: 700px;
  height: 450px;
  width: 700px;
  background-color: white;
  border-radius: 40px;
}

.login-card__div__header {
  padding-bottom: 20px;
}

.login-card__div__right {
  padding-bottom: 20px;
}

.login-card__div__form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.login-card__div__form__btn {
  width: 200px;
  height: 35px;
  border-radius: 30px;
  border: none;
  color: white;
  background-color: #2b54c4;
  text-align: center;
  opacity: 1;
  cursor: pointer;
  transition: 0.5s;
}
.login-card__div__form__btn:hover {
  opacity: 0.7;
  width: 260px;
}

.login-card__div__form__btn span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
  font-size: 16px;
}

.login-card__div__form__btn span:after {
  content: "\00bb";
  font-size: 30px;
  position: absolute;
  opacity: 0;

  bottom: -8px;
  right: -15px;
  transition: 0.5s;
}

.login-card__div__form__btn:hover span {
  padding-right: 25px;
}

.login-card__div__form__btn:hover span:after {
  opacity: 1;
  right: 0;
}
.login-card__div__form__input {
  width: 270px;
  height: 80px;
}
.login-card__div__img {
  border-radius:10px;
}

.input-file-button{
  margin-top: 10px;
  padding: 6px 25px;
  background-color:#3d46c8;
  border-radius: 10px;
  color: white;
  cursor: pointer;
  transition: 0.7s;
  opacity: 1;
}

.input-file-button:hover {
  opacity: 0.7;
  background-color: #305c9f;
}
</style>
