<template>
  <div>
    <v-text-field
      v-model="search"
      flat
      v-debounce:1000="call_search"
      dense
      clearable
      solo-inverted
      hide-details
      prepend-inner-icon="mdi-magnify"
      label="Search News"
      class="hidden-sm-and-down mt-2"
    ></v-text-field>
    <div class="text-center mt-2" v-if="loading">
      <v-progress-circular
        class="mt-2"
        size="25"
        indeterminate
        color="primary"
      ></v-progress-circular>
    </div>
    <template v-if="result.length >= 1">
      <div v-for="i in result" v-bind:key="i.id">
        <v-card outlined class="mt-2">
          <!-- <v-card-title><a :href="i.url">{{ i.title }}</a></v-card-title>
          <v-card-subtitle
            >{{ i.source }} - {{ i.publishedAt }}</v-card-subtitle
          >
          <v-card-text>{{ i.description }}</v-card-text>
          <v-card-text>{{ i.description }}</v-card-text> -->
          <v-list-item three-line>
            <v-list-item-content>
              <div class="text-overline mb-4">
                {{ i.source }}
              </div>
              <v-list-item-title class="text-h5 mb-1">
                <a target="__blank__" :href="i.url">{{ i.title }}</a>
              </v-list-item-title>
              <v-list-item-subtitle>{{ i.description }}</v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-avatar tile size="80" color="grey"
              ><v-img :src="i.urlToImage"></v-img
            ></v-list-item-avatar>
          </v-list-item>
          <v-card-actions>
            <v-spacer></v-spacer>
            <HighlightNews :project="project" :news="i"/>
          </v-card-actions>
        </v-card>
      </div>
    </template>
    <template v-else-if="!loading && result.length == 0"
      ><center><b class="mt-3">No Result</b></center></template
    >
  </div>
</template>

<script>
import { UserMixins } from "../../mixins/user";
import HighlightNews from './HighlightNews.vue'

export default {
  mixins: [UserMixins],
  components: {
      HighlightNews
  },
  data() {
    return {
      search: "",
      result: [],
      loading: false,
    };
  },
  props: {
      project : {default: null}
  },
  methods: {
    call_search() {
      this.loading = true;
      this.GET_News("?search=" + this.search).then((data) => {
        console.log(data);
        this.loading = false;
        this.result = data.data;
      });
    },
  },
};
</script>

<style>
</style>