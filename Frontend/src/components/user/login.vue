<template>
  <v-main>
    <v-container>
      <v-layout row wrap align-center>
        <v-flex xs8 sm4 offset-sm2 align-center justify-center>
          <h1>로그인</h1>
          <br />

          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="id"
              :counter="16"
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
export default {
  name: "Userlogin",
  data: () => ({
    valid: false,
    // name rule
    id: "",
    idRules: [
      (v) => !!v || "ID is required",
      (v) => (v && v.length <= 16) || "ID must be less than 16 characters",
    ],
    // password rule
    show1: false,
    password: "",
    rules: {
      required: (value) => !!value || "Password is Required.",
      min: (v) => 4 <= v.length <= 12 || "Max 12 characters",
      emailMatch: () => `The email and password you entered don't match`,
    },
  }),
  methods: {
    validate() {
      console.log("id : ", this.id);
      console.log("password : ", this.password);
      this.$refs.form.validate();

      if (this.$refs.form.validate() == true) {
        alert("로그인 성공");
        this.$router.push({ name: "Home" });
      }
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
