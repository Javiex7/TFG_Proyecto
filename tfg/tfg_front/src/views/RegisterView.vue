<template>
  <div class="container mt-5">
    <span><h1>Nuevo usuario</h1></span>
    <div class="row d-flex justify-content-center">
      <div class="col-md-6">
        <div class="card px-5 py-5">
          <div class="form-data">
            <div class="forms-inputs mb-4">
              <span><b>- Correo</b></span>
              <input
                class="label_margin"
                autocomplete="off"
                type="text"
                v-model="email"
                v-bind:class="{
                  'form-control': true,
                  'is-invalid': !validEmail(email) && emailBlured,
                }"
                v-on:blur="emailBlured = true"
              />
              <div class="invalid-feedback">
                Utiliza un correo electrónico válido
              </div>
            </div>
            <div class="forms-inputs mb-4">
              <span><b>- Contraseña</b></span>
              <input
                class="label_margin"
                autocomplete="off"
                type="password"
                v-model="password"
                v-bind:class="{
                  'form-control': true,
                  'is-invalid': !validPassword(password) && passwordBlured,
                }"
                v-on:blur="passwordBlured = true"
              />
              <div class="invalid-feedback">
                La contraseña debe tener más de 8 caracteres
              </div>
            </div>
            <div class="mb-3">
              <button
                v-on:click.stop.prevent="submit"
                class="btn btn-dark w-100"
              >
                Registrarse!
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: function () {
    return {
      email: "",
      emailBlured: false,
      valid: false,
      password: "",
      passwordBlured: false,
    };
  },

  methods: {
    validate: function () {
      this.emailBlured = true;
      this.passwordBlured = true;
      if (this.validEmail(this.email) && this.validPassword(this.password)) {
        this.valid = true;
      }
    },

    validEmail: function (email) {
      var re = /(.+)@(.+){2,}\.(.+){2,}/;
      if (re.test(email.toLowerCase())) {
        return true;
      }
    },

    validPassword: function (password) {
      if (password.length > 7) {
        return true;
      }
    },

    submit: function () {
      this.validate();
      if (this.valid) {
        const formData = {
          username: this.email,
          password: this.password,
          email: this.email,
        };

        const path = "http://localhost:8000/auth/users/";

        axios
          .post(path, formData)
          .then((response) => {
            this.$router.push("/login");
            console.log("Register user: ", response);
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>

<style>
.label_margin {
  margin-top: 1rem;
}
.forms-inputs {
  text-align: left;
}
</style>
