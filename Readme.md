# Call API Action - GitHub Action

This GitHub Action does customizable API requests against an RestAPI.   

***The API needs to response with valid JSON***  

## Inputs

- `api-url`: RestAPI URL against which oyur requests are made **(required)**.
- `headers`: Headers to send in your HTTP request e.g. Authorization.
- `http-method`: Which HTTP method to use for the requests **(required)**.
- `request-body`: Data to send to the API (needs to be JSON).
- `query-params`: Query params to use for the request.

## Outputs

- `response_data`: The JSON response of the RestAPI.  

This can be further looked at e.g. with jq or something..  

## Example Usage

```yaml
name: Call API Action

on:
  workflow_dispatch:
  push:
    branches:
      - master

jobs:
  call-api:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      # Use the call-api-action
      - name: Get data from API
        id: api_call
        uses: xamma/call-api-action@v1.0.1
        with:
          api-url: 'https://pokeapi.co/api/v2/pokemon'  # URL of the RestAPI
          http-method: 'GET'  # Use GET HTTP Method
          query-params: '{"limit": "10", "offset": "0"}'  # Optional query params
          request-body: ''  # not needed/used, empty string by default
          headers: '' # not needed/used, empty string by default

      - name: Output results
        run: |
          echo "API call completed."
          echo "Response Data: ${{ steps.api_call.outputs.response_data }}"

      - name: Get specific data
        run: |
          first_pokemon_name=$(echo "${{ steps.api_call.outputs.response_data }}" | jq -r '.results[0].name')
          echo "First Pokemon Name: $first_pokemon_name"
          echo "POKE_NAME=$first_pokemon_name" >> $GITHUB_ENV

      # global usable ENV var
      - name: Use the ENV var
        run: |
          echo "The Pokemon name stored in ENV variable is: $POKE_NAME"
```