<template>
<div>
    <div class="text-center mt-2" v-if="loading">
      <v-progress-circular
        class="mt-2"
        size="25"
        indeterminate
        color="primary"
      ></v-progress-circular>
    </div>
    <div v-if="ProjectNews">
    <v-card elevation="0" v-for="i in ProjectNews" v-bind:key="i.id">
      <v-list-item three-line>
        <v-list-item-content>
          <div class="text-overline mb-4">
            {{ i.news_ser.source }}
          </div>
          <v-list-item-title class="text-h5 mb-1">
            <a target="__blank__" :href="i.news_ser.url">{{ i.news_ser.title }}</a>
          </v-list-item-title>
          <v-list-item-subtitle>{{ i.news_ser.description }}</v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-avatar tile size="80" color="grey"
          ><v-img :src="i.news_ser.urlToImage"></v-img
        ></v-list-item-avatar>
      </v-list-item>
      <v-card-actions>
        <v-spacer></v-spacer>
        <HighlightNews :Readonly="false" :commentDB="i.highlight.data"  :news="i.news_ser" />
      </v-card-actions>
    </v-card>
  </div>
</div>
  
</template>

<script>
import { UserMixins } from "../../mixins/user";
import HighlightNews from './HighlightNews.vue'

export default {
  mixins: [UserMixins],
  data() {
    return {
      ProjectNews: null,
      loading: false
    };
  },
  components:{
      HighlightNews
  },
  props: {
    news: { default: null },
    project: { default: null },
  },
  mounted() {
      this.loading = true
    this.GET_ProjectNews().then((data) => {
        this.loading = false
      this.ProjectNews = data.data;
    });
  },
};
</script>

<style>
</style>