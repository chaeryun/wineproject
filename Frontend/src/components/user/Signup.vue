<template>
  <v-main>
    <v-container>
      <v-layout row wrap align-center>
        <v-flex xs12 sm8 offset-sm2 align-center justify-center>
          <h1>회원가입</h1>
          <br />

          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="id"
              :counter="12"
              :rules="idRules"
              label="ID"
              required
            ></v-text-field>

            <v-text-field
              v-model="password"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :rules="[rules.required, rules.min]"
              :type="show1 ? 'text' : 'password'"
              name="input-10-1"
              label="Password"
              hint="At least 8 characters"
              counter
              @click:append="show1 = !show1"
            ></v-text-field>

            <v-text-field
              v-model="nickname"
              :counter="8"
              :rules="nicknameRules"
              label="Nickname"
              required
            ></v-text-field>

            <v-text-field
              v-model="email"
              :rules="emailRules"
              label="E-mail"
              required
            ></v-text-field>

            <!-- <v-select
          v-model="select"
          :items="items"
          :rules="[(v) => !!v || 'Item is required']"
          label="Item"
          required
        ></v-select> -->

            <v-checkbox
              v-model="checkbox"
              :rules="[(v) => !!v || 'You must agree to continue!']"
              label="개인정보 수집 및 이용에 동의합니다."
              required
            ></v-checkbox>

            <v-btn
              :disabled="!valid"
              color="success"
              class="mr-4"
              @click="validate"
            >
              Signup
            </v-btn>

            <v-btn color="error" class="mr-4" @click="reset"> Cancel </v-btn>
          </v-form>
        </v-flex>
      </v-layout>
    </v-container>
  </v-main>
</template>
<script>
export default {
  name: "Signup",
  data: () => ({
    valid: false,
    // name rule
    id: "",
    idRules: [
      (v) => !!v || "ID is required",
      (v) => (v && v.length <= 12) || "ID must be less than 12 characters",
    ],

    // password rule
    show1: false,
    password: "",
    rules: {
      required: (value) => !!value || "Password is Required.",
      min: (v) => v.length <= 8 || "Max 8 characters",
      emailMatch: () => `The email and password you entered don't match`,
    },

    // nickname rule
    nickname: "",
    nicknameRules: [
      (v) => !!v || "Nickname is required",
      (v) => (v && v.length <= 8) || "Nickname must be less than 8 characters",
    ],

    // email rule
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
    // select: null,
    // items: ["Item 1", "Item 2", "Item 3", "Item 4"],
    checkbox: false,
  }),
  methods: {
    validate() {
      console.log("id : ", this.id);
      console.log("password : ", this.password);
      console.log("nickname : ", this.nickname);
      console.log("email : ", this.email);
      this.$refs.form.validate();

      if (this.$refs.form.validate() == true) {
        alert("회원가입성공");
      }
    },
    reset() {
      this.$router.push({ name: "Home" });
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
