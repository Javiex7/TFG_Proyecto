<template>
  <b-container
    class="col-xl-7"
    style="
      padding-top: 2.5rem;
      padding-bottom: 2.5rem;
      padding-left: 1rem;
      padding-right: 1rem;
    "
  >
    <b-alert class="custom-alert" v-model="showSaveAlert" dismissible>
      Cambios guardados <i class="bi bi-cloud-check-fill"></i>
    </b-alert>

    <b-container style="padding: 2rem" class="background-profile">
      <b-row class="align-items-center">
        <!-- Main image -->
        <b-col lg="4">
          <p style="margin: 0rem">
            <i style="font-size: 9rem" class="bi bi-person-vcard-fill"></i>
          </p>
        </b-col>

        <!-- Edit profile -->
        <b-col lg="8">
          <b-row>
            <h3 class="text-start">Perfil de usuario</h3>
          </b-row>

          <b-row class="justify-content-center" style="padding-top: 0.75rem">
            <div class="forms-inputs mb-4">
              <span><b>- Correo</b></span>
              <input
                v-if="userProfile"
                :placeholder="userProfile.user.email"
                class="label_margin"
                type="text"
                v-model="newEmail"
                v-bind:class="{
                  'form-control': true,
                  'is-invalid':
                    !validEmail(newEmail) && emailBlured && newEmail,
                }"
                v-on:blur="emailBlured = true"
              />
              <div class="invalid-feedback">
                Utiliza un correo electrónico válido
              </div>
              <b-button
                style="margin-top: 1rem"
                @click="patchUserProfile('ChangeEmail')"
                variant="primary"
                >Guardar
              </b-button>
            </div>
          </b-row>

          <b-row class="justify-content-center" style="padding-top: 1rem">
            <div class="forms-inputs mb-4">
              <span><b>- Grupo</b></span>
              <input
                v-if="userProfile"
                :placeholder="userProfile.group"
                class="label_margin"
                type="text"
                v-model="newGroup"
                v-bind:class="{ 'form-control': true }"
                v-on:blur="emailBlured = true"
              />
              <b-button
                style="margin-top: 1.25rem"
                @click="patchUserProfile('ChangeGroup')"
                variant="primary"
                >Cambiar grupo de trabajo
              </b-button>
              <b-button
                style="margin-top: 1.25rem; margin-left: 1rem"
                type="link"
                href="/ranking"
                variant="secondary"
                >Ranking
              </b-button>
            </div>
          </b-row>
        </b-col>
      </b-row>

      <!-- Login/Logout -->
      <b-row>
        <b-container class="text-end" style="padding-top: 3rem">
          <b-button v-bind:href="'/login/'" variant="dark"
            >Login / Logout
          </b-button>
        </b-container>
      </b-row>

      <!-- Obtained points -->
      <b-row style="padding: 0rem">
        <b-container class="text-start" style="padding-top: 3rem">
          <b-container v-if="userProfile && userProfile.points">
            <h3>Puntos actuales</h3>
            <h3>
              <b-badge
                class="highlightText"
                v-if="userProfile"
                variant="dark"
                pill
              >
                {{ userProfile.points }} Puntos <i class="bi bi-stars"></i>
              </b-badge>
            </h3>
          </b-container>

          <b-container
            style="margin-top: 2rem"
            v-if="userProfile && userProfile.obtained_points"
          >
            <h3>Puntos máximos obtenidos</h3>
            <h3>
              <b-badge class="highlightText" variant="dark" pill>
                {{ userProfile.obtained_points }} Puntos
                <i class="bi bi-stars"></i>
              </b-badge>
            </h3>
          </b-container>
        </b-container>
      </b-row>

      <!-- Point packs -->
      <b-row style="margin-top: 4rem">
        <b-row style="margin-bottom: 1rem">
          <h3 class="text-start">Paquetes comprados</h3>
        </b-row>

        <b-card-group
          v-if="userProfile && userProfile.purchased_packs.length > 0"
          deck
        >
          <label v-for="pack in userProfile.purchased_packs" :key="pack.id">
            <p style="margin: 1.5rem">
              <b-card
                no-body
                class="overflow-hidden"
                style="max-width: 18rem"
                border-variant="secondary"
              >
                <b-row no-gutters align-v="center">
                  <b-card-body :title="pack.name" class="text-center">
                    <b-button
                      v-bind:href="'/packs/' + pack.id"
                      variant="primary"
                      >Acceder
                    </b-button>
                  </b-card-body>
                </b-row>
              </b-card>
            </p>
          </label>
        </b-card-group>

        <b-row v-else-if="userProfile">
          <p class="text-start">
            - No tienes paquetes comprados, gana puntos y obtén paquetes de
            diferentes categorías.
          </p>
        </b-row>
      </b-row>
    </b-container>
  </b-container>
</template>

<style scoped>
.background-profile {
  background-color: rgba(0, 0, 0, 0.075);
  border-radius: 3rem;
}
</style>

<script>
import axios from "axios";
import Constants from "@/constants";

export default {
  data: function () {
    return {
      userProfile: null,
      newEmail: "",
      emailBlured: false,
      newGroup: "",
      valid: false,
      showSaveAlert: false,
    };
  },

  methods: {
    validate: function () {
      this.emailBlured = true;
      if (this.validEmail(this.newEmail)) {
        this.valid = true;
      }
    },

    validEmail: function (email) {
      var re = /(.+)@(.+){2,}\.(.+){2,}/;
      if (re.test(email.toLowerCase())) {
        return true;
      }
    },

    setUserProfileInfo() {
      const path = Constants.API_URL + "profiles/getDetailedProfile/";

      const headers = {
        Authorization: "Token " + this.$store.state.token,
      };

      axios
        .get(path, { headers })
        .then((response) => {
          this.userProfile = response.data;
        })
        .catch((error) => {
          if (error.response && error.response.status == 401) {
            localStorage.clear();
            this.$router.push({ path: "/login", replace: true });
          }
        });
    },

    patchUserProfile(patchType) {
      const path = Constants.API_URL + "profiles/updateProfile/";

      const headers = {
        Authorization: "Token " + this.$store.state.token,
      };

      const parameters = {};

      if (patchType === "ChangeGroup") {
        if (this.newGroup && this.newGroup != this.userProfile.group) {
          parameters.group = this.newGroup;
        } else {
          alert("Introduce un grupo válido/distinto");
          return;
        }
      } else if (patchType === "ChangeEmail") {
        if (this.newEmail && this.newEmail != this.userProfile.user.email) {
          this.validate();
          if (!this.valid) return;

          if (
            confirm("¿Seguro que quieres cambiar tu correo asociado?") == false
          )
            return;

          parameters.email = this.newEmail;
        } else {
          alert("Introduce un email válido/diferente");
          return;
        }
      } else {
        return;
      }

      axios
        .patch(path, parameters, { headers })
        .then((response) => {
          this.userProfile = response.data;
          this.$root.updateUserInfo();

          this.showSaveAlert = true;

          this.newEmail = "";
          this.newGroup = "";

          window.scrollTo(0, 0);
        })
        .catch((error) => {
          if (
            error.response.data &&
            error.response.data === "That user email has already been taken"
          ) {
            alert(
              "Ya existe un usuario con ese correo asociado. Intenta con otro correo diferente."
            );
            this.newEmail = "";
          } else {
            console.log(error);
          }
        });
    },
  },

  created() {
    this.setUserProfileInfo();
  },
};
</script>
