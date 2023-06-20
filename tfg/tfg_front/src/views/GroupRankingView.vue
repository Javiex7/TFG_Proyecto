<template>
  <b-container style="padding: 1rem">
    <!-- User group ranking -->
    <b-row style="margin-top: 1rem">
      <h3 class="text-start">
        Ranking grupal <i class="bi bi-file-bar-graph-fill"></i>
      </h3>
    </b-row>
    <b-row style="margin-top: 1rem">
      <b-container v-if="ranking">
        <b-table
          style="margin-top: 1rem"
          striped
          hover
          :items="ranking"
          :fields="rankingFields"
        >
          <!-- Index -->
          <template #cell(index)="profile">
            {{ profile.index + 1 }}
          </template>

          <!-- Email -->
          <template #cell(user)="profile">
            <b-row class="justify-content-center">
              <b-col class="max_length">{{ profile.value.email }}</b-col>
            </b-row>
          </template>
        </b-table>
      </b-container>
      <b-container v-else>
        <p>Ranking no disponible, prueba más tarde o <u> con otro grupo</u>.</p>
        <b-button v-bind:href="'/profile'" variant="secondary"
          >Volver a tu perfil
        </b-button>
      </b-container>
    </b-row>
  </b-container>
</template>

<style scoped>
.max_length {
  text-align: center;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  width: 18rem;
}
</style>

<script>
import axios from "axios";
import Constants from "@/constants";

export default {
  data() {
    return {
      ranking: null,
      rankingFields: [
        {
          key: "index",
          label: "",
          sortable: false,
        },
        {
          key: "user",
          label: "Usuario",
          sortable: false,
        },
        {
          key: "obtained_points",
          label: "Puntos máx.",
          sortable: false,
        },
      ],
    };
  },

  methods: {
    getRanking() {
      const path = Constants.API_URL + "profiles/getRanking/";

      const headers = {
        Authorization: "Token " + this.$store.state.token,
      };

      axios
        .get(path, { headers })
        .then((response) => {
          this.ranking = response.data;
        })
        .catch((error) => {
          if (error.response && error.response.status == 401) {
            localStorage.clear();
            this.$router.push({ path: "/login", replace: true });
          }
        });
    },
  },

  created() {
    if (this.$store.state.isAuthenticated) {
      this.getRanking();
    } else {
      localStorage.clear();
      this.$router.push({ path: "/login", replace: true });
    }
  },
};
</script>
