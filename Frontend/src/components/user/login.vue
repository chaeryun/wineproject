<template>
  <v-main>
    <v-container>
      <v-layout row wrap align-center>
        <v-flex xs8 sm4 offset-sm2 align-center justify-center>
          <h1>로그인</h1>
          <br />

          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="user.id"
              :counter="16"
              :rules="idRules"
              label="ID"
              required
            ></v-text-field>

            <v-text-field
              v-model="user.password"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :rules="[rules.required, rules.min]"
              :type="show1 ? 'text' : 'password'"
              name="input-10-1"
              label="Password"
              hint="At least 4 characters ~ 12 characters"
              counter
              @click:append="show1 = !show1"
            ></v-text-field>

            <v-btn
              :disabled="!valid"
              color="success"
              class="mr-4"
              @click="validate"
            >
              Login
            </v-btn>

            <v-btn color="error" class="mr-4" @click="signup"> Signup </v-btn>
          </v-form>
        </v-flex>
      </v-layout>
    </v-container>
  </v-main>
</template>

<script>
import http from "@/util/http-common";
import jwt_decode from "jwt-decode";
// import { mapActions } from "vuex";

export default {
  name: "Userlogin",
  data: () => ({
    valid: false,
    // name rule
    idRules: [
      (v) => !!v || "ID is required",
      (v) => (v && v.length <= 16) || "ID must be less than 16 characters",
    ],
    // password rule
    show1: false,
    rules: {
      required: (value) => !!value || "Password is Required.",
      min: (v) => 4 <= v.length <= 12 || "Max 12 characters",
      emailMatch: () => `The email and password you entered don't match`,
    },

    user: {
      id: "",
      password: "",
    },
  }),

  computed: {
    // ...mapState(memberStore, ["isLogin"]),
    userstate() {
      return this.$store.state.userstate;
    },
  },

  methods: {
    // ...mapActions(["getUserInfo"]),

    validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate() == true) {
        this.login();
      }
    },

    async login() {
      await http({
        method: "post",
        url: "/accounts/login/",
        data: {
          username: this.user.id,
          password: this.user.password,
        },
      })
        .then((res) => {
          //sessionStore token저장
          let token = res.data.token;
          sessionStorage.setItem("access-token", token);

          //store에 저장
          this.$store.commit("userstate", true);
          if (this.userstate.islogin) {
            alert("로그인 성공");
            this.saveuser(token);
            this.$router.push({ name: "Home" });
          } else {
            alert("아이디나 비밀번호 확인");
          }

          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    async saveuser(token) {
      let decode_token = jwt_decode(token);
      console.log("decode_token", decode_token);

      await http({
        method: "get",
        url: "accounts/get_user/" + decode_token.username,
        // params: {
        //   username: decode_token.username,
        // },
      })
        .then((res) => {
          // store에 user정보 저장
          const userdata = res.data;
          this.$store.commit("user", userdata);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    signup() {
      this.$router.push({ name: "Signup" });
    },
  },
};
</script>

<style scoped>
.v-text-field {
  width: 600px;
  height: 90px;
}
</style>
