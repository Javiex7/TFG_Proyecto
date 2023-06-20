<template>
  <b-container style="padding: 1rem">
    <h1 style="padding: 2rem">Nuevo usuario</h1>
    <b-row class="justify-content-center">
      <b-col lg="5" md="8">
        <b-card>
          <b-container>
            <b-row class="justify-content-center">
              <div class="forms-inputs mb-4">
                <span><b>- Correo</b></span>
                <input
                  class="label_margin"
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
            </b-row>

            <b-row style="margin-bottom: 1rem" class="justify-content-center">
              <b-col cols="8">
                <div style="margin-top: 1rem">
                  <b-button
                    v-on:click.stop.prevent="submit"
                    class="btn btn-dark w-100"
                    variant="primary"
                  >
                    Crear usuario
                  </b-button>
                </div>
              </b-col>
            </b-row>
          </b-container>
        </b-card>
      </b-col>
    </b-row>

    <b-row style="margin-top: 2rem" class="justify-content-center">
      <p>
        Ya tienes cuenta ->
        <a class="custom-a" href="/login">Iniciar sesión</a>
      </p>
    </b-row>
  </b-container>
</template>

<script>
import axios from "axios";
import Constants from "@/constants";

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
      if (this.$store.state.isAuthenticated) {
        alert("Antes de crear un nuevo usuario debes cerrar sesión");
        this.$router.push("/login");
      }
      if (this.valid) {
        const formData = {
          username: this.email,
          password: this.password,
          email: this.email,
        };

        const path = Constants.AUTH_URL + "users/";

        axios
          .post(path, formData)
          .then(() => {
            this.$router.push("/login");
          })
          .catch((error) => {
            if (!error.response) return;

            console.log(error);

            switch (error.response.status) {
              case 400:
                if (
                  error.response.data.username &&
                  error.response.data.username[0] ===
                    "A user with that username already exists."
                ) {
                  alert(
                    "Ya existe un usuario con ese correo asociado. Intenta con otro correo o pide ayuda a tu administrador."
                  );
                } else {
                  alert("Ups, ha ocurrido un error inesperado.");
                  localStorage.clear();
                  this.$router.go();
                }
                break;

              default:
                alert("Ups, ha ocurrido un error inesperado.");
                localStorage.clear();
                this.$router.go();
            }
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
