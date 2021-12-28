<template>
  <div>
    <v-row>
      <v-col cols="12" sm="12">
        <v-card >
          <v-card-title class="white--text primary">
            Research Projects

            <v-spacer></v-spacer>

            <AddProject />
          </v-card-title>

          <v-card-text>
            <ViewProject class="mt-1" />
          </v-card-text>
        </v-card>
      </v-col>

      <!-- <v-col cols="12" sm="6">
         <stories />
      </v-col> -->
    </v-row>
  </div>
</template>

<script>
import AddProject from "../components/Project/AddProject.vue";
import ViewProject from "../components/Project/ViewProject.vue";

export default {
  name: "Home",

  components: {
    AddProject,
    ViewProject,
  },
};
</script>
