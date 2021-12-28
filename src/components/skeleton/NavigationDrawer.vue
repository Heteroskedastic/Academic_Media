<template>
  <v-navigation-drawer
    floating
    clipped
    width="280"
    v-model="ComputedDrawer"
    app
  >
    <v-sheet v-if="Userinfo_getters" color="grey lighten-4" class="pa-4">
      <v-avatar class="mb-4" color="grey darken-1" size="64"
        >{{
          Userinfo_getters.email ? Userinfo_getters.email[0] : "" | uppercase
        }}
      </v-avatar>

      <div>{{ Userinfo_getters.email ? Userinfo_getters.email : "" }}</div>
      <div class="text-caption">
        {{ Userinfo_getters.type ? Userinfo_getters.type : "" }}
      </div>
      <div class="text-caption">
        Last Login:
        {{ Userinfo_getters.last_login ? Userinfo_getters.last_login : "" }} 
        <!-- <v-btn color="primary" x-small outlined>Logout</v-btn> -->
      </div>
    </v-sheet>
    <!--  -->
    <v-list rounded dense>
      <!-- <v-subheader>REPORTS</v-subheader> -->
      <v-list-item-group v-model="value" color="primary">
        <v-list-item v-for="(item, i) in items" :key="i">
          <v-list-item-icon>
            <v-icon v-text="item.icon"></v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { SkeletonMixins } from "../../mixins/skeleton";
import { UserMixins } from "../../mixins/user";

export default {
  mixins: [SkeletonMixins, UserMixins],
  data() {
    return {
      value: "",
      items: [
        // { text: "Search", icon: "mdi-search-web" }
      ],
    };
  },
};
</script>

<style>
</style>