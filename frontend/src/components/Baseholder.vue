<template>
  <div v-if="hasParams()">
    <b-card 
      style="width: 20rem; height: 15rem" 
      class="text-center" 
      v-bind:header= "items.name"
      border-variant="dark"
      bg-variant="light">
    <b-card-text class="text-left">
      {{shortenDescript()}}
        <div v-if= "hasEventParams()">
        Place: {{items.place}} <br>
        Start Time: {{items.starttime}} <br>
        End Time: {{items.starttime}}
        </div>
    </b-card-text>
    <div v-if= "!isEvent">
    <b-button v-bind:to="link" class="mt-auto">To club Page</b-button>
    </div>
  </b-card>
    
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'Baseholder',
  props: ['items', 'isEvent'],
  data: function() {
    return {
      property: this.items
    }
  },
  methods:
  {
      hasParams: function() 
      {
          if(this.items && this.items.name
            && this.items.description)
            {
                return true;
            }
            return false;
      },
      hasEventParams: function() 
      {
          if(this.items && this.items.place
            && this.items.starttime && this.items.endtime)
            {
                return true;
            }
            return false;
      },
      shortenDescript: function ()
      {
          if(this.items.description.length > 110)
          {
            var sub=  this.items.description.substring(0,110);
            var index = sub.lastIndexOf(' ');
            return sub.substring(0,index).concat("...");
          }
          else
          {
            return this.items.description;
          }

      }

  },
  computed:
  {
      link: function()
      {
          return "club/" + encodeURI(this.items.name);
      }

  }
}

</script scoped>
.card {
  border: 2px;
}
</style>