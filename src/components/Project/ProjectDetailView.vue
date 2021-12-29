<template>
  <div>
    <v-breadcrumbs :items="items" divider="/"></v-breadcrumbs>

    <v-card elevation="0">
      <v-card-title># {{ ProjectDetails && ProjectDetails.name ?  ProjectDetails.name : '' }}</v-card-title>
      <v-card-text>
        <v-tabs v-model="tab">
          <v-tab>News</v-tab>
          <v-tab>Add News</v-tab>
          <v-tab>Questions</v-tab>
        </v-tabs>

        <v-tabs-items v-model="tab">
          <v-tab-item>
            <viewNews :project="projectId" />
          </v-tab-item>
          <v-tab-item>
            <search :project="projectId" />
          </v-tab-item>
        </v-tabs-items>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import search from "../News/SearchNews.vue";
import viewNews from "../News/ViewNewsPage.vue";
import { UserMixins } from "../../mixins/user";

export default {
  mixins: [UserMixins],
  components: {
    search,
    viewNews
  },
  data() {
    return {
      projectId: null,
      ProjectDetails: null,
      tab: null,
      items: [
        {
          text: "Home",
          disabled: false,
          href: "/#/",
        },
        {
          text: "Project Edit",
          disabled: true,
          href: "breadcrumbs_link_1",
        },
      ],
    };
  },
  mounted() {
    this.projectId = this.$route.params.id;
    this.GET_USER_Project_ID(this.projectId+'/')
    .then(data => {
      this.ProjectDetails = data.data
    })
  },
};
</script>

<style>
</style>