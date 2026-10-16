# IS-2 — How does a Spring Security application integrate with Okta and OAuth 2.0?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.7 | [4:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=259s) | 🟢 USEFUL | Okta OAuth authorization server |
| YT-1.8 | [4:57](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=297s) | 🟢 USEFUL | Authentication redirect and authorization flow |
| YT-1.9 | [5:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=321s) | 🟢 USEFUL | Callback URLs and identity-provider configuration |
| YT-1.10 | [6:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=394s) | 🟢 USEFUL | Frontend-to-Okta-to-backend flow |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [4:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=259s) uh I generally used uh OCTA o 2.0 U that's that's that's I think that's one of the popularly getting used uh<br>[4:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=272s) authentication and authorization tool so and it's uh spring also comes with a spring security uh which I prefer like also return on top of this so this is the main thing which I have used correct<br>[4:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=286s) I agree that OCTA you have used as authorization servers and Spring Security is something which properly integrates with the OCTA parts so yes completely agree on that front now my | I use Okta to handle sign-in, while Spring Security protects the API. For example, a user clicks Login, signs in through Okta, and the application receives tokens through the configured OAuth/OpenID Connect flow. When the user calls our order API, the backend validates the access token and checks permissions. For a browser app, I would normally use authorization code with PKCE. Okta confirms who signed in; our API still decides what that person can do. |

## Video option — YT-3: Mock Interview | Core Java Mock Interview Question and Answers | Code Decode ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=d22oNW1W6ms)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.14 | [12:37](https://www.youtube.com/watch?v=d22oNW1W6ms&t=757s) | 🟢 USEFUL | How do OAuth 2.0, OpenID Connect, and Okta fit together? |
| YT-3.15 | [13:52](https://www.youtube.com/watch?v=d22oNW1W6ms&t=832s) | 🟢 USEFUL | Follow-up: How do OAuth 2.0, OpenID Connect, and Okta fit together? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [12:50](https://www.youtube.com/watch?v=d22oNW1W6ms&t=770s) so what format of token you have used for communication what type of token is it is it a basic like see basic 64 encoded token or a proper JWT token yeah the proper JWT token we had<br>[13:06](https://www.youtube.com/watch?v=d22oNW1W6ms&t=786s) used okay and U you have so how these U communication goes so you have told me about the authorization part that you have Ro based access controls over your apis but how is authentication done for | OAuth 2.0 provides delegated authorization, while OpenID Connect adds an identity layer for sign-in. Okta can act as the provider issuing tokens. For example, a frontend signs users in through Okta and sends an access token to a Spring API. The API validates the token and checks scopes or roles. |

