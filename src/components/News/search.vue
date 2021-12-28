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
        <div v-for="i in result" v-bind:key="i.id">
            <v-card outlined class="mt-2">
          <v-card-title>{{i.title}}</v-card-title>
          <v-card-subtitle>{{i.source}}-{{i.publishedAt}}</v-card-subtitle>
          <v-card-text>{{i.content}}</v-card-text>
        </v-card>
        </div>
  </div>
</template>

<script>
import { UserMixins } from "../../mixins/user";

export default {
        mixins: [UserMixins],
data(){
    return{
        search: '',
        result: [],
    }
},
   methods: {
       call_search(){
           this.GET_News('?search='+this.search)
           .then(data => {
               console.log(data)
               this.result = data.data
           })
       }
   }
}
</script>

<style>

</style>