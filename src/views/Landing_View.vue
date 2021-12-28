<template>
  <v-app >

    <NavigationDrawer/>
    <AppBar/>

    <v-main>
      <v-container  fluid>
        <router-view/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import NavigationDrawer from '../components/skeleton/NavigationDrawer.vue'
import AppBar from '../components/skeleton/AppBar.vue'
import { UserMixins } from "../mixins/user";

export default {
  mixins: [UserMixins],
  components:{
    NavigationDrawer,
    AppBar
  },
  data: () => ({
    
  }),
  mounted(){
    this.GET_USER_API();
  },
  methods:{
    
  }
};
</script>