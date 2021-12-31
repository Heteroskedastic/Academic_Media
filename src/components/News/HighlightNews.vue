<template>
  <div class="text-center">
    <v-dialog fullscreen v-model="dialog" width="900" height="900">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          v-bind="attrs"
          v-on="on"
          title="Add Projcet"
          color="primary"
          class="text--white"
          small
        >
          {{Readonly ? 'Select' : 'View'}}
        </v-btn>
      </template>

      <v-card>
          <v-toolbar
          dark
          color="primary"
        >
          <v-btn
            icon
            dark
            @click="dialog = false"
          >
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title>{{ Readonly?  'Add News to Project': 'View News' }}</v-toolbar-title>
          <v-spacer></v-spacer>
          
        </v-toolbar>

  

        <v-card-text>
          <v-list-item three-line>
            <v-list-item-content>
              <div class="text-overline mb-4">
                {{ news.source }}
              </div>
              <v-list-item-title class="text-h5 mb-1">
                <a target="__blank__" :href="news.url">{{ news.title }}</a>
              </v-list-item-title>
            </v-list-item-content>

            <v-list-item-avatar tile size="80" color="grey"
              ><v-img :src="news.urlToImage"></v-img
            ></v-list-item-avatar>
          </v-list-item>

          <!-- v menu -->
          <v-row>
            <v-col v-if="Readonly" cols="12" sm="6">
              <v-menu
                v-model="menu"
                :nudge-width="20"
                :close-on-content-click="false"
                offset-x
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-textarea
                    style="cursor: none"
                    hint="add Highlight news by selecting word"
                    persistent-hint
                    v-bind="attrs"
                    v-on="on"
                    @select.native="selectText"
                    v-model="news.description"
                  ></v-textarea>
                </template>

                <v-card>
                  <v-list>
                    <v-list-item>
                      <!-- <v-list-item-avatar>
                    <img
                      src="https://cdn.vuetifyjs.com/images/john.jpg"
                      alt="John"
                    />
                  </v-list-item-avatar> -->

                      <v-list-item-content>
                        <v-list-item-title>{{
                          selecredWord
                        }}</v-list-item-title>
                        <v-list-item-subtitle>
                          <v-text-field
                            v-model="comment"
                            label="Comment"
                          ></v-text-field>
                        </v-list-item-subtitle>
                      </v-list-item-content>

                      <!-- <v-list-item-action>
                    <v-btn
                      :class="fav ? 'red--text' : ''"
                      icon
                      @click="fav = !fav"
                    >
                      <v-icon>mdi-heart</v-icon>
                    </v-btn>
                  </v-list-item-action> -->
                    </v-list-item>
                  </v-list>

                  <v-card-actions>
                    <v-spacer></v-spacer>

                    <v-btn text @click="menu = false"> Cancel </v-btn>
                    <v-btn
                      color="primary"
                      text
                      @click="
                        menu = false;
                        addcomment();
                      "
                    >
                      Add
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-menu>
            </v-col>
            <v-col cols="12" sm="6">
            <b v-if="Readonly">Preview:  </b>
              <br />
              <div  v-html="highlight()"></div>
            </v-col>
          </v-row>

          <!-- <v-textarea
            readonly
            @select.native="selectText"
            v-model="news.description"
          ></v-textarea> -->
        </v-card-text>

        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn v-if="Readonly" :loading="saveloading" color="primary" @click="SaveProjectNews">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>


<script>
import { UserMixins } from "../../mixins/user";

export default {
  mixins: [UserMixins],

  data() {
    return {
      load: true,
      dialog: false,
      saveloading: false,
      RequiredRules: [(v) => !!v || "Required"],
      payload: {
        name: null,
      },
      ProjectNews: {
        highlight: null,
        project: null,
        news: null,
      },
      fav: true,
      menu: false,
      message: false,
      hints: true,
      commenList: [],
      selecredWord: "",
      comment: "",
      query: "joe",
    };
  },
  props: {
    news: { default: null },
    project: { default: null },
    commentDB: { default: null },
    Readonly: { default: true },
  },
  mounted() {
    if (this.commentDB) {
      this.commenList = this.commentDB;
    }
  },
  methods: {
    SaveProjectNews() {
        this.saveloading = true
      this.ProjectNews.highlight = { data: this.commenList };
      this.ProjectNews.project = this.project;
      this.ProjectNews.news = this.news.id;
      this.POST_USER_ProjectNews(this.ProjectNews).then(() => {
          this.dialog = false
          this.saveloading = false
      });
    },
    selectText(e) {
      console.log(e);
      var start = e.target.selectionStart;
      var end = e.target.selectionEnd;
      this.selecredWord = e.target.value.substring(start, end);
    },
    addcomment() {
      console.log(this.selecredWord, this.comment);
      this.commenList.push({ word: this.selecredWord, comment: this.comment });
      this.comment = null;
    },
    highlight() {
      var html = "";
      if (this.commenList.length >= 1) {
        for (var i of this.commenList) {
          if (!i.word) {
            return this.news.description;
          }
          html =
            html +
            this.news.description.replace(new RegExp(i.word, "gi"), (match) => {
              var temp = '<div class="tooltip highlightText">'+ match +'<span class="tooltiptext">'+i.comment+'</span></div>'
              return temp
              
            });
        }
        return html;
      } else {
        return this.news.description;
      }
    },
    addProject() {
      if (this.$refs.addprojectref.validate()) {
        this.POST_USER_Project(this.payload).then(() => {
          this.dialog = false;
          this.GET_USER_Project();
        });
      }
    },
  },
};
</script>

<style>
.highlightText {
  background: yellow;
}
.tooltip {
  position: relative;
  display: inline-block;
  border-bottom: 1px dotted black;
}

.tooltip .tooltiptext {
  visibility: hidden;
  width: 120px;
  background-color: black;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 5px 0;
  position: absolute;
  z-index: 1;
  bottom: 150%;
  left: 50%;
  margin-left: -60px;
}

.tooltip .tooltiptext::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: black transparent transparent transparent;
}

.tooltip:hover .tooltiptext {
  visibility: visible;
}
</style>