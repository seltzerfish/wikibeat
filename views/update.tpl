% rebase("layout.tpl", title="Store App - Update")
% if "permissions" in sess and sess["permissions"] == "MANAGER":
<div class="container">
  <div class="row">
    <div class="twelve column" style="margin-top: 10%">
      <h4 style="text-align: center">Update product: {{item_data['name']}}</h4>
    </div>
  </div>
  <form action="/update/{{item_data['id']}}" method="POST">
    <fieldset>
      <div class="row" style="margin-top: 5%">
        <div class="six columns">
          <label for="name">Product Name</label>
          <input class="u-full-width" id="name" type="text" value="{{item_data['name']}}" name="name">
        </div>
        <div class="three columns">
          <label for="quantity">Quantity</label>
          <input class="u-full-width" id="quantity" type="number" value="{{item_data['quantity']}}" name="quantity">
        </div>
        <div class="three columns">
          <label for="price">Price (without '$')</label>
          <input class="u-full-width" id="price" type="text" value="{{item_data['price']}}" name="price">
        </div>
      </div>
      <div class="row" style="margin-top: 5%">
        <div class="six columns">
          <label for="provider">Provider</label>
          <input class="u-full-width" id="provider" type="text" value="{{item_data['provider']}}" name="provider">
        </div>
        <div class="six columns">
          <label for="provider_contact">Provider Telephone Number</label>
          <input class="u-full-width" id="provider_contact" type="tel" value="{{item_data['provider_contact']}}" name="provider_contact">
        </div>
      </div>
      <a class="button" href="/" style="margin: 3%; margin-left: 0%">Cancel</a>
      <input class="button-primary" type="submit" value="Update">
    </fieldset>
  </form>
</div>
% else:
% include('denied.tpl')
