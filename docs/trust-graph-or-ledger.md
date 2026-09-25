# ⚖️ Trust graph or promise ledger: which to build

> **Unverified.** Bill's analysis, 2026-09-24. Reviews the
> [trust graph POC](https://app.notion.com/p/c231e4e6dec04385acb0b6e8adef649b) and the
> [promise ledger](promise-ledger.md).
>
> Imported from Notion on 2026-09-25:
> [original page](https://app.notion.com/p/d6b662a172104f00a6c65cc7d41f4106).

**These are not two projects.** The promise ledger is the first three weekends of the
trust graph POC. The graph is the ledger plus a schema, code, and a trust calculation on
top. The decision is whether you stop at the data or keep going.

That makes one direction reversible and the other not.

## What the ledger asks

Four questions per bet:

1. Was it built?
2. What did it cost, and when did it arrive?
3. Did it answer the question it was sold on?
4. Whose call was it?

## What already exists

| Source | What it covers |
|---|---|
| [Pan and Trimble 2024](https://baas.aas.org/pub/2024i006/release/1), BAAS 56(1), extending [Trimble 2011](https://arxiv.org/pdf/2311.02950) | Every prioritized facility from seven decadal surveys under "what they asked for" and "what we got." Across 106 requests in the first five reports: roughly a third operating within 15 years on mostly federal money, a third later or with other funding, a third never happened |
| [CATE](https://www.nationalacademies.org/read/24857/chapter/5), required since the 2008 NASA Authorization Act | An independent cost estimate for every candidate mission, built to be compared against what advocates claimed. Run by Aerospace Corporation |
| Midterm assessments: [Astro2010](https://www.nationalacademies.org/projects/DEPS-SSB-14-05/publication/23560), [planetary](https://www.nationalacademies.org/read/25186/chapter/8), [Earth science](https://www.nationalacademies.org/read/27743/chapter/12) | Progress against recommendations, with cost and schedule sections |
| [Powering Science: NASA's Large Strategic Science Missions](https://www.nationalacademies.org/read/24857/chapter/5), NASEM 2017 | Cost overruns in large NASA missions |

Questions 1 and 2 are covered. What is open:

- **The science question.** Pan and Trimble ask whether the winners were worth having,
  judged by productivity and prestige. Nobody checks a facility against the specific
  promise written in the report.
- **P5.** All of the above is astronomy and space science. Particle physics
  self-assessment is P5 reaffirming P5.
- **Attribution.** These count facilities, not forecasters. That is the trust graph's
  core idea and the piece with no prior art.
- **Maintenance.** Pan and Trimble is a commentary by two authors, not a living dataset.

## Cost

| | Promise ledger | Trust graph POC |
|---|---|---|
| Work | 3 weekends: extract, verify, link | The same 3, plus 2 to 4 for schema, code, and math |
| Skill used | Research, reading, source hunting | The above, plus building |
| Technical risk | None | Moderate. Weekend code projects stall |
| Hardest part | Judging whether a science question got answered. Needs domain judgment you do not have | Too little data. 20 bets and roughly 40 people cannot support person-level trust |
| Failure mode | You stall on the science question and ship nothing | You ship a schema demo and present it as evidence |

## Benefit

| | Promise ledger | Trust graph POC |
|---|---|---|
| Audience | Physicists, astronomers, decadal and P5 people, funders, Convergent, IFP | Paul, metascience tool builders, enterprise context-layer people |
| Novelty | Partial. Built and cost are covered. The science question and attribution are open | Contested. ORKG, nanopublications, scite, discourse graphs, and Epoch each hold a piece |
| What it proves about you | You can measure allocation in a field that does not measure itself | You can design and build a system |
| Conversation value | A reason to write to any physicist, repeatedly, one question per bet | One strong conversation with Paul |
| Clears your compensation requirement | No. Public good, no buyer | Only in the enterprise framing, which is a different build |
| Fits the position you landed on | Yes. Allocation measurement | Partly. Sits closer to publishing reform |

## When each wins

**The ledger wins if** your goal is standing with physicists and astronomers, you want
repeated low-stakes contact rather than one reveal, weekend time is scarce and you need
guaranteed output, or you are genuinely unsure. It is the reversible move, since the
ledger feeds the graph either way.

**The graph wins if** the real goal is a product and a co-founder rather than a
community position, you want the enterprise angle that pays, Paul is the single most
valuable thread and you want to meet him as a peer designer rather than a data
contributor, or you know you will finish code on weekends.

## Recommendation

Ledger, scoped hard.

1. **Start from Pan and Trimble.** Their table is the seed for built and cost. Cite it,
   extend it to P5, and spend the saved time on the science question.
2. **The science question is the artifact.** Three to five bets where the report named
   something specific: dark energy's equation of state, neutrino mass ordering,
   primordial gravitational waves. Small n, deep, unoccupied.
3. **Attribute.** Record who championed each bet and who sat on the panel. Publishing
   names is a separate decision, but without the people this is a facilities table.
4. **Run extraction through two models with hand checks** for the model trust dataset.

Good enough is five bets scored on the science question with attribution, plus a
one-page scorecard citing Pan and Trimble for the rest. That ships, and it is the
attachment for the Paul email.

## The third option

The enterprise credibility layer is the only one of the three that clears your
compensation requirement, and it overlaps your day job. The todo is at
[Review the enterprise credibility and context layer (Glean, Microsoft)](https://app.notion.com/p/65f5cc02697349eea1c1ace7ed9484ad).
It is not what you asked to choose between, but if the answer to "artifact or company"
is company, neither option above is the right build.

## Questions for you

1. **What is this artifact's job:** getting you into conversations, or getting you into a company?
2. **How many weekend blocks actually exist** before year end? Three versus seven settles this on its own.
3. **Do you want to write code on weekends?** Honest answer. The graph is not worth doing halfway.
4. **Is Paul the main thread or one of several?** If main, the graph is the peer
   artifact. If one of several, the ledger travels further.
5. **Will you make the call on whether a science question got answered,** knowing
   physicists may disagree with you? If not, the ledger loses its open ground and needs a
   physicist collaborator.
6. **Named committees and people, or aggregate only?** This decides whether the ledger is shareable or stays internal.
7. **Is there a date driving this?** Neither will be ready for FORRT next week, so if
   something else is creating urgency, name it.
