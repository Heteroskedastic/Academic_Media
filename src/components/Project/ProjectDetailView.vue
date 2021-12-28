<template>
  <div>
    <v-card elevation="0">
      <v-card-title># {{ projectId }}</v-card-title>
      <v-card-text>
        <v-tabs v-model="tab">
          <v-tab>News</v-tab>
          <v-tab>Questions</v-tab>
        </v-tabs>

        <v-tabs-items v-model="tab">
          <v-tab-item>
              <search/>
          </v-tab-item>
        </v-tabs-items>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>

import search from "../News/search.vue";

export default {
    components: {
        search
    },
  data() {
    return {
      projectId: null,
      tab: null,
    };
  },
  mounted() {
    this.projectId = this.$route.params.id;
  },
};
</script>

<style>
</style>