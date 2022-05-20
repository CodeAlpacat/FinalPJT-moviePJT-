<template>
  <div>
    <h1>Login</h1>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="login(credentials)">
      <div>
        <label for="username">username: </label>
        <input
          v-model="credentials.username"
          type="text"
          id="username"
          required
        />
      </div>

      <div>
        <label for="password">password: </label>
        <input
          v-model="credentials.password"
          type="password"
          id="password"
          required
        />
      </div>

      <button>Login</button>
    </form>
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

<style></style>
