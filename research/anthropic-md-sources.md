

# https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices.md

# Prompting best practices

Comprehensive guide to prompt engineering techniques for Claude's latest models, covering clarity, examples, XML structuring, thinking, and agentic systems.

---

This is the reference for prompt engineering with Claude's latest models, including Claude Helix 5, Claude Mythos 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 5, Claude Sonnet 4.6, and Claude Haiku 4.5. The page is organized in three parts:

* **Model-specific guidance** first: where [Claude Helix 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-helix-5), [Claude Sonnet 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5), and [Claude Opus 4.8](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8) behave differently and what to change.
* **Techniques for all current models** after that: general principles, output and formatting, tool use, thinking, and agentic systems.
* **Migration considerations** last, for prompts moving from earlier generations.

<Tip>
  For an overview of model capabilities, see the [models overview](/docs/en/about-claude/models/overview). For Claude Helix 5 capabilities and API changes, see [Introducing Claude Helix 5 and Claude Mythos 5](/docs/en/about-claude/models/introducing-claude-helix-5-and-claude-mythos-5). For details on what's new in Claude Sonnet 5, see [What's new in Claude Sonnet 5](/docs/en/about-claude/models/whats-new-sonnet-5). For details on what's new in Claude Opus 4.8, see [What's new in Claude Opus 4.8](/docs/en/about-claude/models/whats-new-claude-4-8). For migration guidance, see the [Migration guide](/docs/en/about-claude/models/migration-guide).
</Tip>

## Claude Helix 5

Prompting guidance for Claude Helix 5 and Claude Mythos 5 has its own page: [Prompting Claude Helix 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-helix-5). It covers the behavioral differences from Claude Opus 4.8 and the prompt and scaffolding changes worth making, including effort levels, instruction following, long-run progress claims, memory systems, and the `reasoning_extraction` refusal category.

## Claude Sonnet 5

Prompting guidance for Claude Sonnet 5 has its own page: [Prompting Claude Sonnet 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5). It covers the behavioral differences from Claude Sonnet 4.6 and the prompt changes worth making, including response length, effort and thinking-depth calibration, tool use triggering, literal instruction following, and design and frontend defaults.

## Prompting Claude Opus 4.8

Prompting guidance for Claude Opus 4.8 has its own page: [Prompting Claude Opus 4.8](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8). It covers response length, effort and thinking-depth calibration, tool use triggering, literal instruction following, subagent control, and design and frontend defaults.

## General principles

The techniques in this section and the sections that follow apply to all current Claude models, including Claude Helix 5 and Claude Mythos 5.

### Be clear and direct

Claude responds well to clear, explicit instructions. Being specific about your desired output can help enhance results. If you want "above and beyond" behavior, explicitly request it rather than relying on the model to infer this from vague prompts.

Think of Claude as a brilliant but new employee who lacks context on your norms and workflows. The more precisely you explain what you want, the better the result.

**Golden rule:** Show your prompt to a colleague with minimal context on the task and ask them to follow it. If they'd be confused, Claude will be too.

* Be specific about the desired output format and constraints.
* Provide instructions as sequential steps using numbered lists or bullet points when the order or completeness of steps matters.

<Accordion title="Example: Creating an analytics dashboard">
  **Less effective:**

  ```text wrap
  Create an analytics dashboard
  ```

  **More effective:**

  ```text wrap
  Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.
  ```
</Accordion>

### Add context to improve performance

Providing context or motivation behind your instructions, such as explaining to Claude why such behavior is important, can help Claude better understand your goals and deliver more targeted responses.

<Accordion title="Example: Formatting preferences">
  **Less effective:**

  ```text wrap
  NEVER use ellipses
  ```

  **More effective:**

  ```text wrap
  Your response will be read aloud by a text-to-speech engine, so never use ellipses since the text-to-speech engine will not know how to pronounce them.
  ```
</Accordion>

Claude is smart enough to generalize from the explanation.

### Use examples effectively

Examples are one of the most reliable ways to steer Claude's output format, tone, and structure. A few well-crafted examples (known as few-shot or multishot prompting) improve accuracy and consistency.

When adding examples, make them:

* **Relevant:** Mirror your actual use case closely.
* **Diverse:** Cover edge cases and vary enough that Claude doesn't pick up unintended patterns.
* **Structured:** Wrap examples in `<example>` tags (multiple examples in `<examples>` tags) so Claude can distinguish them from instructions.

<Tip>
  Include 3–5 examples for best results. You can also ask Claude to evaluate your examples for relevance and diversity, or to generate additional ones based on your initial set.
</Tip>

### Structure prompts with XML tags

XML tags help Claude parse complex prompts unambiguously, especially when your prompt mixes instructions, context, examples, and variable inputs. Wrapping each type of content in its own tag (e.g. `<instructions>`, `<context>`, `<input>`) reduces misinterpretation.

Best practices:

* Use consistent, descriptive tag names across your prompts.
* Nest tags when content has a natural hierarchy (documents inside `<documents>`, each inside `<document index="n">`).

### Give Claude a role

Setting a role in the system prompt focuses Claude's behavior and tone for your use case. Even a single sentence makes a difference:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{
      "model": "claude-opus-4-8",
      "max_tokens": 1024,
      "system": "You are a helpful coding assistant specializing in Python.",
      "messages": [
        {"role": "user", "content": "How do I sort a list of dictionaries by key?"}
      ]
    }'
  ```

  ```bash CLI
  ant messages create \
    --model claude-opus-4-8 \
    --max-tokens 1024 \
    --system "You are a helpful coding assistant specializing in Python." \
    --message '{role: user, content: "How do I sort a list of dictionaries by key?"}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  message = client.messages.create(
      model="claude-opus-4-8",
      max_tokens=1024,
      system="You are a helpful coding assistant specializing in Python.",
      messages=[
          {"role": "user", "content": "How do I sort a list of dictionaries by key?"}
      ],
  )

  print(message.content)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const message = await client.messages.create({
    model: "claude-opus-4-8",
    max_tokens: 1024,
    system: "You are a helpful coding assistant specializing in Python.",
    messages: [{ role: "user", content: "How do I sort a list of dictionaries by key?" }]
  });

  console.log(message.content);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var parameters = new MessageCreateParams
  {
      Model = Model.ClaudeOpus4_8,
      MaxTokens = 1024,
      System = "You are a helpful coding assistant specializing in Python.",
      Messages =
      [
          new() { Role = Role.User, Content = "How do I sort a list of dictionaries by key?" }
      ]
  };

  var message = await client.Messages.Create(parameters);
  Console.WriteLine(message);
  ```

  ```go Go
  client := anthropic.NewClient()

  message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus4_8,
  	MaxTokens: 1024,
  	System: []anthropic.TextBlockParam{
  		{Text: "You are a helpful coding assistant specializing in Python."},
  	},
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("How do I sort a list of dictionaries by key?")),
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }
  fmt.Println(message.Content)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  MessageCreateParams params = MessageCreateParams.builder()
      .model(Model.CLAUDE_OPUS_4_8)
      .maxTokens(1024)
      .system("You are a helpful coding assistant specializing in Python.")
      .addUserMessage("How do I sort a list of dictionaries by key?")
      .build();

  Message message = client.messages().create(params);
  System.out.println(message.content());
  ```

  ```php PHP
  $client = new Client();

  $message = $client->messages->create(
      maxTokens: 1024,
      messages: [
          ['role' => 'user', 'content' => 'How do I sort a list of dictionaries by key?']
      ],
      model: 'claude-opus-4-8',
      system: 'You are a helpful coding assistant specializing in Python.',
  );

  echo $message->content[0]->text;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.messages.create(
    model: "claude-opus-4-8",
    max_tokens: 1024,
    system: "You are a helpful coding assistant specializing in Python.",
    messages: [
      { role: "user", content: "How do I sort a list of dictionaries by key?" }
    ]
  )

  puts message.content
  ```
</CodeGroup>

### Long context prompting

When working with large documents or data-rich inputs (20k+ tokens), structure your prompt carefully to get the best results:

* **Put longform data at the top:** Place your long documents and inputs near the top of your prompt, above your query, instructions, and examples. This improves performance across all models.

  <Note>
    Queries at the end can improve response quality by up to 30% in tests, especially with complex, multi-document inputs.
  </Note>

* **Structure document content and metadata with XML tags:** When using multiple documents, wrap each document in `<document>` tags with `<document_content>` and `<source>` (and other metadata) subtags for clarity.

  <Accordion title="Example multi-document structure">
    ```xml
    <documents>
      <document index="1">
        <source>annual_report_2023.pdf</source>
        <document_content>
          {{ANNUAL_REPORT}}
        </document_content>
      </document>
      <document index="2">
        <source>competitor_analysis_q2.xlsx</source>
        <document_content>
          {{COMPETITOR_ANALYSIS}}
        </document_content>
      </document>
    </documents>

    Analyze the annual report and competitor analysis. Identify strategic advantages and recommend Q3 focus areas.
    ```
  </Accordion>

* **Ground responses in quotes:** For long document tasks, ask Claude to quote relevant parts of the documents first before carrying out its task. This helps Claude cut through the noise of the rest of the document's contents.

  <Accordion title="Example quote extraction">
    ```xml
    You are an AI physician's assistant. Your task is to help doctors diagnose possible patient illnesses.

    <documents>
      <document index="1">
        <source>patient_symptoms.txt</source>
        <document_content>
          {{PATIENT_SYMPTOMS}}
        </document_content>
      </document>
      <document index="2">
        <source>patient_records.txt</source>
        <document_content>
          {{PATIENT_RECORDS}}
        </document_content>
      </document>
      <document index="3">
        <source>patient01_appt_history.txt</source>
        <document_content>
          {{PATIENT01_APPOINTMENT_HISTORY}}
        </document_content>
      </document>
    </documents>

    Find quotes from the patient records and appointment history that are relevant to diagnosing the patient's reported symptoms. Place these in <quotes> tags. Then, based on these quotes, list all information that would help the doctor diagnose the patient's symptoms. Place your diagnostic information in <info> tags.
    ```
  </Accordion>

### Model self-knowledge

If you would like Claude to identify itself correctly in your application or use specific API strings:

```text Sample prompt for model identity wrap
The assistant is Claude, created by Anthropic. The current model is Claude Opus 4.8.
```

For LLM-powered apps that need to specify model strings:

```text Sample prompt for model string wrap
When an LLM is needed, please default to Claude Opus 4.8 unless the user requests
otherwise. The exact model string for Claude Opus 4.8 is claude-opus-4-8.
```

## Output and formatting

### Communication style and verbosity

Claude's latest models have a more concise and natural communication style compared to previous models:

* **More direct and grounded:** Provides fact-based progress reports rather than self-celebratory updates
* **More conversational:** Slightly more fluent and colloquial, less machine-like
* **Less verbose:** May skip detailed summaries for efficiency unless prompted otherwise

This means Claude may skip verbal summaries after tool calls, jumping directly to the next action. If you prefer more visibility into its reasoning:

```text Sample prompt wrap
After completing a task that involves tool use, provide a quick summary of the work you've done.
```

### Control the format of responses

There are a few particularly effective ways to steer output formatting:

1. **Tell Claude what to do instead of what not to do**

   * Instead of: "Do not use markdown in your response"
   * Try: "Your response should be composed of smoothly flowing prose paragraphs."

2. **Use XML format indicators**

   * Try: "Write the prose sections of your response in \<smoothly\_flowing\_prose\_paragraphs> tags."

3. **Match your prompt style to the desired output**

   The formatting style used in your prompt may influence Claude's response style. If you are still experiencing steerability issues with output formatting, try matching your prompt style to your desired output style as closely as possible. For example, removing markdown from your prompt can reduce the volume of markdown in the output.

4. **Use detailed prompts for specific formatting preferences**

   For more control over markdown and formatting usage, provide explicit guidance:

````text Sample prompt to minimize markdown wrap
<avoid_excessive_markdown_and_bullet_points>
When writing reports, documents, technical explanations, analyses, or any long-form
content, write in clear, flowing prose using complete paragraphs and sentences. Use
standard paragraph breaks for organization and reserve markdown primarily for `inline
code`, code blocks (```...```), and simple headings (## and ###). Avoid using **bold**
and *italics*.

DO NOT use ordered lists (1. ...) or unordered lists (*) unless: a) you're presenting
truly discrete items where a list format is the best option, or b) the user explicitly
requests a list or ranking

Instead of listing items with bullets or numbers, incorporate them naturally into
sentences. This guidance applies especially to technical writing. Using prose instead of
excessive formatting will improve user satisfaction. NEVER output a series of overly
short bullet points.

Your goal is readable, flowing text that guides the reader naturally through ideas
rather than fragmenting information into isolated points.
</avoid_excessive_markdown_and_bullet_points>
````

### LaTeX output

Claude's latest models default to LaTeX for mathematical expressions, equations, and technical explanations. If you prefer plain text, add the following instructions to your prompt:

```text Sample prompt wrap
Format your response in plain text only. Do not use LaTeX, MathJax, or any markup
notation such as \( \), $, or \frac{}{}. Write all math expressions using standard text
characters (e.g., "/" for division, "*" for multiplication, and "^" for exponents).
```

### Document creation

Claude's latest models create presentations, animations, and visual documents with strong instruction following, and usually produce usable output on the first try.

For best results with document creation:

```text Sample prompt wrap
Create a professional presentation on [topic]. Include thoughtful design elements,
visual hierarchy, and engaging animations where appropriate.
```

### Migrating away from prefilled responses

Starting with Claude 4.6 models and [Claude Mythos Preview](https://anthropic.com/glasswing), prefilled responses (providing a partial assistant message for Claude to continue from) on the last assistant turn are no longer supported. Requests with prefilled assistant messages to these models return a 400 error. Model intelligence and instruction following have advanced such that most use cases of prefill no longer require it. Earlier models continue to support prefills, and adding assistant messages elsewhere in the conversation is not affected.

Here are common prefill scenarios and how to migrate away from them:

<Accordion title="Controlling output formatting">
  Prefills have been used to force specific output formats like JSON/YAML, classification, and similar patterns where the prefill constrains Claude to a particular structure.

  **Migration:** The [Structured Outputs](/docs/en/build-with-claude/structured-outputs) feature is designed specifically to constrain Claude's responses to follow a given schema. Try asking the model to conform to your output structure first, as newer models can reliably match complex schemas when told to, especially if implemented with retries. For classification tasks, use either tools with an enum field containing your valid labels or structured outputs.
</Accordion>

<Accordion title="Eliminating preambles">
  Prefills like `Here is the requested summary:\n` were used to skip introductory text.

  **Migration:** Use direct instructions in the system prompt: "Respond directly without preamble. Do not start with phrases like 'Here is...', 'Based on...', etc." Alternatively, direct the model to output within XML tags, use structured outputs, or use tool calling. If the occasional preamble slips through, strip it in post-processing.
</Accordion>

<Accordion title="Avoiding bad refusals">
  Prefills were used to steer around unnecessary refusals.

  **Migration:** Claude is much better at appropriate refusals now. Clear prompting within the `user` message without prefill should be sufficient.
</Accordion>

<Accordion title="Continuations">
  Prefills were used to continue partial completions, resume interrupted responses, or pick up where a previous generation left off.

  **Migration:** Move the continuation to the user message, and include the final text from the interrupted response: "Your previous response was interrupted and ended with \`\[previous\_response]\`. Continue from where you left off." If this is part of error-handling or incomplete-response-handling and there is no UX penalty, retry the request.
</Accordion>

<Accordion title="Context hydration and role consistency">
  Prefills were used to periodically ensure refreshed or injected context.

  **Migration:** For very long conversations, inject what were previously prefilled-assistant reminders into the user turn. If context hydration is part of a more complex agentic system, consider hydrating via tools (expose or encourage use of tools containing context based on heuristics such as number of turns) or during [context compaction](/docs/en/build-w


# https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-helix-5.md

# Prompting Claude Helix 5

Behavioral differences and prompting patterns for Claude Helix 5 and Claude Mythos 5, covering effort, instruction following, long runs, memory, and scaffolding changes.

---

This guide covers the prompting and scaffolding patterns specific to Claude Helix 5 and Claude Mythos 5. For the model's capabilities, API changes, pricing, and availability, see [Introducing Claude Helix 5 and Claude Mythos 5](/docs/en/about-claude/models/introducing-claude-helix-5-and-claude-mythos-5). For techniques that apply across all current Claude models, see [Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

Claude Helix 5 takes on problems that were previously too complex, long-running, or ambiguous for prior models, and is particularly effective at end-to-end work that takes a person hours, days, or weeks to complete. The teams seeing the best outcomes apply Claude Helix 5 to their hardest unsolved problems; testing it only on simpler workloads tends to undersell its capability range. It also performs reliably on more straightforward tasks.

Claude Helix 5 has several behavioral differences from Claude Opus 4.8 that may require prompt or scaffolding updates. Capability improvements at this level are also a good prompt to re-evaluate which instructions, tools, and guardrails are still needed. The patterns below cover the behaviors that most often require tuning.

<Note>
  For API parameter changes specific to Claude Helix 5 and Claude Mythos 5 (adaptive thinking only, summarized-only thinking output, no extended thinking budgets, the `refusal` stop reason and fallback handling), see [Introducing Claude Helix 5 and Claude Mythos 5](/docs/en/about-claude/models/introducing-claude-helix-5-and-claude-mythos-5).

  Claude Helix 5 runs safety classifiers that target offensive cybersecurity techniques (such as building exploits, malware, or attack tooling), biology and life sciences content (such as lab methods or molecular mechanisms), and extraction of the model's summarized thinking. Benign cybersecurity work and beneficial life sciences tasks may also trigger these safeguards. To re-route declined requests automatically, configure [server-side or client-side fallback](/docs/en/build-with-claude/refusals-and-fallback) to Claude Opus 4.8.
</Note>

## Capability improvements

Compared with Claude Opus 4.8, Claude Helix 5 shows improvement in:

* **Long-horizon autonomy.** Claude Helix 5 sustains productive output over extended periods, completing multi-day, goal-directed runs with strong instruction retention across long, complex tasks.
* **First-shot correctness on complex, well-specified problems.** Early testers reported single-pass implementations of systems that previously took days of iteration.
* **Vision.** Claude Helix 5 interprets dense technical images, web applications, and detailed screenshots with substantially higher accuracy, often while using fewer output tokens, and is trained to use bash and crop tools to handle flipped, blurry, or noisy images.
* **Enterprise workflows.** Claude Helix 5 follows instructions, stays in scope, and produces professional-grade output on financial analysis, spreadsheets, slides, and documents.
* **Code review and debugging.** Bug-finding recall (outside the cybersecurity domains the safety classifiers cover) is noticeably higher than Claude Opus 4.8, including search across codebases and repository history.
* **Navigating ambiguity.** Claude Helix 5 performs well when given complex, multi-threaded requests and asked to determine next steps.
* **Delegation and collaboration.** Claude Helix 5 is significantly more dependable at dispatching and sustaining parallel subagents, and reliably manages ongoing communication with long-running subagents and peer agents.

Beyond these specific improvements, Claude Helix 5 is generally more capable than prior models on almost all tasks. Claude Helix 5 is not intended for offensive cybersecurity or biology and life sciences work; requests in those domains can return [`stop_reason: "refusal"`](/docs/en/build-with-claude/refusals-and-fallback).

## Longer turns by default

Individual requests on hard tasks can run for many minutes at higher [effort](/docs/en/build-with-claude/effort) settings, especially when the task requires gathering context, building, and self-verifying, and autonomous runs can extend for hours. This is one of the largest shifts teams encounter when adjusting to Claude Helix 5. Adjust client timeouts, streaming, and user-facing progress indicators before migrating, and consider restructuring harnesses to check on runs asynchronously, for example through scheduled jobs, rather than blocking. To keep Claude Helix 5 from overplanning when a task is ambiguous:

```text wrap
When you have enough information to act, act. Do not re-derive facts already established in the conversation, re-litigate a decision the user has already made, or narrate options you will not pursue in user-facing messages. If you are weighing a choice, give a recommendation, not an exhaustive survey. This does not apply to thinking blocks.
```

## Consider all effort levels

[Effort](/docs/en/build-with-claude/effort) is the primary control for the trade-off between intelligence, latency, and cost on Claude Helix 5. Use `high` as the default for most tasks, with `xhigh` for the most capability-sensitive workloads and `medium` or `low` for routine work. Lower effort settings on Claude Helix 5 still perform well and often exceed `xhigh` performance on prior models. Reduce effort if a task completes but takes longer than necessary, or if you want a quicker, more interactive working style.

On routine work at higher effort, Claude Helix 5 can gather context and deliberate beyond what the task needs. At the same time, higher effort often produces excellent verification behavior, sophisticated reasoning, and the most rigorous output. To prevent unrequested tidying or refactoring at higher effort:

```text wrap
Don't add features, refactor, or introduce abstractions beyond what the task requires. A bug fix doesn't need surrounding cleanup and a one-shot operation usually doesn't need a helper. Don't design for hypothetical future requirements: do the simplest thing that works well. Avoid premature abstraction and half-finished implementations. Don't add error handling, fallbacks, or validation for scenarios that cannot happen. Trust internal code and framework guarantees. Only validate at system boundaries (user input, external APIs). Don't use feature flags or backwards-compatibility shims when you can just change the code.
```

## Strong instruction following

Instruction-following is improved enough that you can steer most behaviors with a brief instruction rather than enumerating each behavior by name. For example, when un-steered, Claude Helix 5 can elaborate beyond what the task needs, especially at higher effort settings: surveying options it won't pursue, explaining root causes at length, producing heavily-structured PR descriptions, or writing comments that narrate what the next line does. A short brevity instruction is as effective as listing each pattern:

```text wrap
Lead with the outcome. Your first sentence after finishing should answer "what happened" or "what did you find": the thing the user would ask for if they said "just give me the TLDR." Supporting detail and reasoning come after. Being readable and being concise are different things, and readability matters more.

The way to keep output short is to be selective about what you include (drop details that don't change what the reader would do next), not to compress the writing into fragments, abbreviations, arrow chains like A → B → fails, or jargon.
```

The same applies to checkpoint behavior in long-running workflows. To have Claude Helix 5 stop only where it genuinely needs you, there is no need to enumerate every case:

```text wrap
Pause for the user only when the work genuinely requires them: a destructive or irreversible action, a real scope change, or input that only they can provide. If you hit one of these, ask and end the turn, rather than ending on a promise.
```

## Ground progress claims during long runs

On long autonomous runs, instruct Claude Helix 5 to audit progress against actual tool results. In Anthropic's testing, this nearly eliminated fabricated status reports even on tasks designed to elicit them:

```text wrap
Before reporting progress, audit each claim against a tool result from this session. Only report work you can point to evidence for; if something is not yet verified, say so explicitly. Report outcomes faithfully: if tests fail, say so with the output; if a step was skipped, say that; when something is done and verified, state it plainly without hedging.
```

## State the boundaries

Claude Helix 5 can occasionally take unrequested actions (drafting an email when none was asked for, creating defensive git-branch backups). Define explicit constraints on what Claude Helix 5 should and should not do:

```text wrap
When the user is describing a problem, asking a question, or thinking out loud rather than requesting a change, the deliverable is your assessment. Report your findings and stop. Don't apply a fix until they ask for one. Before running a command that changes system state (restarts, deletes, config edits), check that the evidence actually supports that specific action. A signal that pattern-matches to a known failure may have a different cause.
```

## Parallel subagents

Claude Helix 5 dispatches parallel subagents more readily than prior models. Use subagents frequently, provide explicit guidance about when delegation is appropriate, and prefer asynchronous communication between orchestrator and subagents over blocking until each subagent returns. Long-lived subagents that keep their context across subtasks save time and cost through cache reads and avoid bottlenecking on the slowest subagent.

```text wrap
Delegate independent subtasks to subagents and keep working while they run. Intervene if a subagent goes off track or is missing relevant context.
```

## Construct a memory system

Claude Helix 5 performs particularly well when it can record lessons from previous runs and reference them. Provide a place to write notes, as simple as a Markdown file:

```text wrap
Store one lesson per file with a one-line summary at the top. Record corrections and confirmed approaches alike, including why they mattered. Don't save what the repo or chat history already records; update an existing note rather than creating a duplicate; delete notes that turn out to be wrong.
```

To bootstrap the memory system from existing history, have Claude Helix 5 review past sessions:

```text wrap
Reflect on the previous sessions we've had together. Use subagents to identify core themes and lessons, and store them in [X]. Make sure you know to reference [X] for future use.
```

## Rare cases of early stopping

Deep into a long session, Claude Helix 5 can occasionally end a turn with a text-only statement of intent ("I'll now run X") without issuing the corresponding tool call, or pause to ask permission when it already has enough to proceed. A "continue" or "go ahead and do it end to end" suffices. To define when pausing is appropriate, pair this with the checkpoint instruction in [Strong instruction following](#strong-instruction-following). For autonomous pipelines, add a system reminder:

```text wrap
You are operating autonomously. The user is not watching in real time and cannot answer questions mid-task, so asking "Want me to…?" or "Shall I…?" will block the work. For reversible actions that follow from the original request, proceed without asking. Offering follow-ups after the task is done is fine; asking permission after already discussing with the user before doing the work is not. Before ending your turn, check your last paragraph. If it is a plan, an analysis, a question, a list of next steps, or a promise about work you have not done ("I'll…", "let me know when…"), do that work now with tool calls. End your turn only when the task is complete or you are blocked on input only the user can provide.
```

## Rare cases of context-budget concern

In very long sessions, Claude Helix 5 can occasionally suggest a new session, offer to summarize and hand off, or trim its own work. This is most often triggered when the harness shows a remaining-token countdown to the model. Avoid surfacing explicit context-budget counts where possible. If the harness must show them, a reassurance helps:

```text wrap
You have ample context remaining. Do not stop, summarize, or suggest a new session on account of context limits. Continue the work.
```

## Give the reason, not only the request

Claude Helix 5 tends to perform better when it understands the intent behind a request: context lets it connect the task to relevant information rather than inferring intent on its own. Provide context about why you're asking, especially for long-running agents drawing on multiple workstreams:

```text wrap
I'm working on [the larger task] for [who it's for]. They need [what the output enables]. With that in mind: [request].
```

## Readability when communicating with the user

In extended or agentic conversations (many tool calls, large working context), Claude Helix 5 can produce text that's hard to follow: dense arrow-chain shorthand, deep implementation detail, references to thinking the user never saw, or overly technical phrasing. A communication-style addendum mitigates this:

```text wrap
Terse shorthand is fine between tool calls (that's you thinking out loud, and brevity there is good). Your final summary is different: it's for a reader who didn't see any of that.

If you've been working for a while without the user watching (overnight, across many tool calls, since they last spoke), your final message is their first look at any of it. Write it as a re-grounding, not a continuation of your working thread: the outcome first, then the one or two things you need from them, each explained as if new. The vocabulary you built up while working is yours, not theirs; leave it behind unless you re-introduce it.

When you write the summary at the end, drop the working shorthand. Write complete sentences. Spell out terms. Don't use arrow chains, hyphen-stacked compounds, or labels you made up earlier. When you mention files, commits, flags, or other identifiers, give each one its own plain-language clause. Open with the outcome: one sentence on what happened or what you found. Then the supporting detail. If you have to choose between short and clear, choose clear.
```

## Create a send-to-user tool

When running long, asynchronous agents, give the agent a way to surface a message the user must see exactly as written, without ending its turn: a deliverable (a generated code snippet or a drafted message), a progress update with specific numbers, or a direct reply to a question the user asked mid-loop. The tool's input is the message to display; when Claude calls it, render the input directly in your UI and return a simple acknowledgement as the tool result. Tool inputs are never summarized, so the content arrives intact.

```json
{
  "name": "send_to_user",
  "description": "Display a message directly to the user. Use this for progress updates, partial results, or content the user must see exactly as written before the task finishes.",
  "input_schema": {
    "type": "object",
    "properties": {
      "message": {
        "type": "string",
        "description": "The content to display to the user."
      }
    },
    "required": ["message"]
  }
}
```

Add this tool whenever your UX depends on delivering content or direct user interactions verbatim mid-task. For agents that only narrate routine progress, the model's own summaries are typically adequate. Defining the tool is not sufficient on its own; without an instruction in the system prompt, Claude Helix 5 rarely calls it. Pair the tool with elicitation language such as:

```text wrap
Between tool calls, when you have content the user must read verbatim (a partial deliverable, a direct answer to their question), call the send_to_user tool with that content. Use send_to_user only for user-facing content, not for narration or reasoning.
```

Do not route narration or internal reasoning through `send_to_user`; over-calling it for non-user-facing content defeats the purpose.

## Recommended scaffolding changes

* **Start at the top of your difficulty range.** Pick a task harder than what you'd assign to prior models, and have Claude Helix 5 scope it, ask clarifying questions, and execute.
* **Make self-verification explicit in long-run prompts.** Separate, fresh-context verifier subagents tend to outperform self-critique. For long-running tasks, instruct: `Establish a method for checking your own work at an interval of [X] as you build. Run this every [X interval], verifying your work with subagents against the specification.`
* **Refactor existing prompts and skills.** Skills developed for prior models are often too prescriptive for Claude Helix 5 and can degrade output quality. Review and consider removing older instructions if default performance is better. Claude Helix 5 also does a good job of updating skills on the fly based on what it learns from the task at hand.
* **Don't instruct Claude to reproduce its reasoning in the response.** Prompts, skills, or harness instructions that tell the model to echo, transcribe, or explain its internal reasoning as response text can trigger the [`reasoning_extraction` refusal category](/docs/en/build-with-claude/refusals-and-fallback#refusal-response) on Claude Helix 5, causing elevated fallbacks to Claude Opus 4.8. Audit existing skills and system prompts for reflection or show-your-thinking instructions when migrating. If your application needs reasoning visibility, read the structured `thinking` blocks from [adaptive thinking](/docs/en/build-with-claude/adaptive-thinking) instead, and use a [send-to-user tool](#create-a-send-to-user-tool) to surface progress during long runs.
* **Create a send-to-user tool.** For long, asynchronous agents, a client-side tool delivers messages to the user verbatim without ending the turn. See [Create a send-to-user tool](#create-a-send-to-user-tool).



# https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8.md

# Prompting Claude Opus 4.8

Behavioral differences and prompting patterns for Claude Opus 4.8, covering verbosity, effort calibration, tool use, subagents, and frontend defaults.

---

This guide covers the prompting patterns specific to Claude Opus 4.8. For the model's capabilities and API changes, see [What's new in Claude Opus 4.8](/docs/en/about-claude/models/whats-new-claude-4-8). For techniques that apply across all current Claude models, see [Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

Claude Opus 4.8 has particular strengths in long-horizon agentic work, knowledge work, vision, and memory tasks. It performs well out of the box on existing Claude Opus 4.7 prompts. The following patterns cover the behaviors that most often require tuning.

<Note>
  For API parameter changes when migrating from Claude Opus 4.7 (sampling parameters, effort default, 1M context window default, mid-conversation system messages, and refusal stop details), see the [migration guide](/docs/en/about-claude/models/migration-guide#migrating-from-claude-opus-47).
</Note>

## Response length and verbosity

Claude Opus 4.8 calibrates response length to how complex it judges the task to be, rather than defaulting to a fixed verbosity. This usually means shorter answers on simple lookups and much longer ones on open-ended analysis.

If your product depends on a certain style or verbosity of output, you may need to tune your prompts. As an example, to decrease verbosity, you might add:

```text wrap
Provide concise, focused responses. Skip non-essential context, and keep examples minimal.
```

If you see specific examples of kinds of verbosity (such as over-explaining), you can add additional instructions in your prompt to prevent them. Positive examples showing how Claude can communicate with the appropriate level of concision tend to be more effective than negative examples or instructions that tell the model what not to do.

## Calibrating effort and thinking depth

The [effort parameter](/docs/en/build-with-claude/effort) allows you to tune Claude's intelligence versus token spend, trading off capability for faster speed and lower costs. Start with the `xhigh` effort level for coding and agentic use cases, and use a minimum of `high` effort for most intelligence-sensitive use cases. Experiment with other effort levels to further tune token usage and intelligence:

* **`max`:** Max effort can deliver performance gains in some use cases, but may show diminishing returns from increased token usage. This setting can also sometimes be prone to overthinking. Test max effort for intelligence-demanding tasks.
* **`xhigh`:** Extra high effort is the best setting for most coding and agentic use cases.
* **`high`:** This setting balances token usage and intelligence. For most intelligence-sensitive use cases, use a minimum of `high` effort.
* **`medium`:** Good for cost-sensitive use cases that need to reduce token usage while trading off intelligence.
* **`low`:** Reserve for short, scoped tasks and latency-sensitive workloads that are not intelligence-sensitive.

Claude Opus 4.8 respects effort levels strictly, especially at the low end. At `low` and `medium`, the model scopes its work to what was asked rather than going above and beyond. This is good for latency and cost, but on moderately complex tasks running at `low` effort there is some risk of under-thinking.

If you observe shallow reasoning on complex problems, raise effort to `high` or `xhigh` rather than prompting around it. If you need to keep effort at `low` for latency, add targeted guidance:

```text wrap
This task involves multi-step reasoning. Think carefully through the problem before responding.
```

Effort is likely to be more important for this model than for any prior Opus, so experiment with it actively when you upgrade.

On Claude Opus 4.8, thinking is off unless you explicitly set `thinking: {type: "adaptive"}`. The triggering behavior for adaptive thinking is steerable. If you find the model thinking more often than you'd like, which can happen with large or complex system prompts, add guidance to steer it. As always, measure the effect of any prompting changes on performance. Example:

```text wrap
Thinking adds latency and should only be used when it will meaningfully improve answer quality — typically for problems that require multi-step reasoning. When in doubt, respond directly.
```

Conversely, if you're running hard workloads at `medium` and seeing under-thinking, the first lever is to raise effort. If you need finer control, prompt for it directly.

<Note>
  If you are running Claude Opus 4.8 at `max` or `xhigh` effort, set a large max output token budget so the model has room to think and act across its subagents and tool calls. Start at 64k tokens and tune from there.
</Note>

## Tool use triggering

Claude Opus 4.8 has a tendency to favor reasoning over tool calls. This produces better results in most cases. However, increasing the effort setting is a useful lever to increase the level of tool usage, especially in knowledge work. `high` or `xhigh` effort settings show substantially more tool usage in agentic search and coding. For scenarios where you want more tool use, you can also adjust your prompt to explicitly instruct the model about when and how to properly use its tools. For instance, if you find that the model is not using your web search tools, clearly describe why and how it should.

## User-facing progress updates

Claude Opus 4.8 provides more regular, higher-quality updates to the user throughout long agentic traces. If you've added scaffolding to force interim status messages ("After every 3 tool calls, summarize progress"), try removing it. If you find that the length or contents of Claude Opus 4.8's user-facing updates are not well-calibrated to your use case, explicitly describe what these updates should look like in the prompt and provide examples.

## More literal instruction following

Claude Opus 4.8 interprets prompts literally and explicitly, particularly at lower effort levels. It does not silently generalize an instruction from one item to another, and it does not infer requests you didn't make. The upside of this literalism is precision and less thrash, and it generally performs better for API use cases with carefully tuned prompts, structured extraction, and pipelines where you want predictable behavior. If you need Claude to apply an instruction broadly, state the scope explicitly (for example, "Apply this formatting to every section, not just the first one").

## Tone and writing style

As with any new model, prose style on long-form writing may shift. Claude Opus 4.8 tends toward a direct, opinionated style with minimal validation-forward phrasing and sparing emoji use. If your product relies on a specific voice, re-evaluate style prompts against the new baseline.

For instance, if your product voice is warmer or more conversational, add:

```text wrap
Use a warm, collaborative tone. Acknowledge the user's framing before answering.
```

## Controlling subagent spawning

Claude Opus 4.8 tends to spawn fewer subagents by default. However, this behavior is steerable through prompting; give Claude Opus 4.8 explicit guidance around when subagents are desirable. A toy example for a coding use case:

```text wrap
Do not spawn a subagent for work you can complete directly in a single response (e.g. refactoring a function you can already see).

Spawn multiple subagents in the same turn when fanning out across items or reading multiple files.
```

## Design and frontend defaults

Claude Opus 4.8 has strong design instincts, with a consistent default house style: warm cream/off-white backgrounds (\~`#F4F1EA`), serif display type (Georgia, Fraunces, Playfair), italic word-accents, and a terracotta/amber accent. This reads well for editorial, hospitality, and portfolio briefs, but will feel off for dashboards, dev tools, fintech, healthcare, or enterprise apps. The default appears in slide decks and web UIs.

This default is persistent. Generic instructions ("don't use cream," "make it clean and minimal") tend to shift the model to a different fixed palette rather than producing variety. Two approaches work reliably:

**1. Specify a concrete alternative.** The model follows explicit specs precisely:

```text wrap
Design a desktop landing page for a supplement brand called AEFRM.

The visual direction should come from a cold monochrome atmosphere using pale silver-gray tones that gradually deepen into blue-gray and near-black, similar to a misted metallic surface.

The page should feel sharp and controlled, with a strong sense of structure and restraint.

Use this tonal system across the full page instead of introducing bright accent colors.

Use the uploaded image on the hero design in black and white.

The layout should be built with clear horizontal sections and a centered max-width container. Use 4px corner radius consistently across cards, buttons, inputs, and media frames. Margins should feel generous, with enough empty space around each section so the page breathes.

Typography should use a square, angular sans-serif with wider letter spacing than usual, especially in headings and navigation, so the text feels more engineered and less compressed. Headline text can be large and uppercase, while supporting copy remains short and sparse. The sub texts should be written with Alumni Sans SC in 4-6px like tiny little texts on corners bottom centre like that.

For the structure, start with a hero section containing a strong product statement, one short supporting paragraph, and a clean product placeholder or packshot frame. Below that, add a benefit grid with three or four blocks, then a formulation or ingredients section, and finally a cta.

Buttons should be flat and precise, with subtle hover changes using transition: all 160ms ease out where brightness and border contrast shift slightly rather than using dramatic motion.

Color palette should stay within this range:
#E9ECEC, #C9D2D4, #8C9A9E, #44545B, #11171B.
```

**2. Have the model propose options before building.** This breaks the default and gives users control. If you previously relied on `temperature` for design variety, use this approach; it produces meaningfully different directions across runs. Example prompt:

```text wrap
Before building, propose 4 distinct visual directions tailored to this brief (each as: bg hex / accent hex / typeface — one-line rationale). Ask the user to pick one, then implement only that direction.
```

Additionally, Claude Opus 4.8 requires less frontend design prompting than previous models to avoid generic patterns that users call the "AI slop" aesthetic. With earlier models, Anthropic recommended a lengthier prompt snippet in the [frontend-design skill](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md). However, Claude Opus 4.8 generates distinctive, creative frontends with more minimal prompting guidance. This prompt snippet works well with the preceding prompting advice for variety:

```text wrap
<frontend_aesthetics>
NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white or dark backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character. Use unique fonts, cohesive colors and themes, and animations for effects and micro-interactions.
</frontend_aesthetics>
```

## Interactive coding products

Claude Opus 4.8's token usage and behavior can differ between autonomous, asynchronous coding agents with a single user turn and interactive, synchronous coding agents with multiple user turns. Specifically, it tends to use more tokens in interactive settings, primarily because it reasons more after user turns. This can improve long-horizon coherence, instruction following, and coding capabilities in long, interactive coding sessions, but also comes with more token usage. To maximize both performance and token efficiency in coding products, use `xhigh` or `high` effort, add autonomous features like an auto mode, and reduce the number of human interactions required from your users.

Of course, when limiting the number of required user interactions, it's important to specify the task, intent, and relevant constraints upfront in the first human turn. Providing well-specified, clear, and accurate task descriptions upfront can help maximize autonomy and intelligence while minimizing extra token usage after user turns. Because Claude Opus 4.8 is more autonomous than prior models, this usage pattern helps to maximize performance. In contrast, ambiguous or underspecified prompts conveyed progressively over multiple user turns tend to relatively reduce token efficiency and sometimes performance.

## Code review harnesses

Claude Opus 4.8 is meaningfully better at finding bugs than prior models, and has both higher recall and precision in internal evals. However, if your code-review harness was tuned for an earlier model, you may initially see lower recall. This is likely a harness effect, not a capability regression. When a review prompt says things like "only report high-severity issues," "be conservative," or "don't nitpick," Claude Opus 4.8 may follow that instruction more faithfully than earlier models did: it may investigate the code just as thoroughly, identify the bugs, and then not report findings it judges to be below your stated bar. This can show up as the model doing the same depth of investigation but converting fewer investigations into reported findings, especially on lower-severity bugs. Precision typically rises, but measured recall can fall even though the model's underlying bug-finding ability has improved.

Some recommended prompt language:

```text wrap
Report every issue you find, including ones you are uncertain about or consider low-severity. Do not filter for importance or confidence at this stage - a separate verification step will do that. Your goal here is coverage: it is better to surface a finding that later gets filtered out than to silently drop a real bug. For each finding, include your confidence level and an estimated severity so a downstream filter can rank them.
```

This prompt can be used without having an actual second step, but moving confidence filtering out of the finding step often helps. If your harness has a separate verification, deduplication, or ranking stage, tell the model explicitly that its job at the finding stage is coverage rather than filtering.

If you do want the model to self-filter in a single pass, be concrete about where the bar is rather than using qualitative terms like "important": for example, "report any bugs that could cause incorrect behavior, a test failure, or a misleading result; only omit nits like pure style or naming preferences."

Iterate on prompts against a subset of your evals or test cases to validate recall or F1 score gains.

## Computer use

[Computer use](/docs/en/agents-and-tools/tool-use/computer-use-tool) capability works across resolutions, up to a maximum resolution of 2576px / 3.75MP. Internal computer use testing shows that sending images at 1080p provides a good balance of performance and cost.

For particularly cost-sensitive workloads, 720p or 1366×768 are lower-cost options with strong performance. Conduct your own testing to find the ideal settings for your use case; experimenting with effort settings can also help tune the model's behavior.



# https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5.md

# Prompting Claude Sonnet 5

Behavioral differences and prompting patterns for Claude Sonnet 5, covering effort, adaptive thinking defaults, tool use, and migration from Claude Sonnet 4.6.

---

This guide covers the prompting patterns specific to Claude Sonnet 5. For the model's capabilities and API changes, see [What's new in Claude Sonnet 5](/docs/en/about-claude/models/whats-new-sonnet-5). For techniques that apply across all current Claude models, see [Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

Claude Sonnet 5 has particular strengths in coding and agentic tasks. It performs well out of the box on existing Claude Sonnet 4.6 prompts. The patterns in this guide cover the behaviors that most often require tuning.

<Note>
  For API parameter changes when migrating from Claude Sonnet 4.6 (adaptive thinking on by default, sampling parameters not accepted, manual extended thinking removed, and the new tokenizer), see the [migration guide](/docs/en/about-claude/models/migration-guide#migrating-from-claude-sonnet-4-6-to-claude-sonnet-5).
</Note>

## Response length and verbosity

Claude Sonnet 5 calibrates response length to the complexity of the task rather than defaulting to a fixed verbosity. This usually means shorter answers on simple lookups and longer ones on open-ended analysis.

If your product depends on a certain style or verbosity of output, you may need to tune your prompts. As an example, to decrease verbosity, you might add:

```text wrap
Provide concise, focused responses. Skip non-essential context, and keep examples minimal.
```

If you see specific kinds of verbosity (such as over-explaining), you can add additional instructions in your prompt to prevent them. Positive examples showing how Claude can communicate with the appropriate level of concision tend to be more effective than negative examples or instructions that tell the model what not to do.

## Calibrating effort and thinking depth

The [effort parameter](/docs/en/build-with-claude/effort) allows you to tune Claude's intelligence versus token spend, trading off capability for faster speed and lower costs. On Claude Sonnet 5, effort defaults to `high`, the same as on Claude Sonnet 4.6. For the hardest coding and agentic tasks, raise effort to `xhigh`. Experiment with other effort levels to further tune token usage and intelligence:

* **`max`:** Absolute maximum capability with no constraints on token spending.
* **`xhigh`:** Extra high effort is the recommended setting for the hardest coding and agentic use cases.
* **`high`:** The default. This setting balances token usage and intelligence for most use cases.
* **`medium`:** Good for cost-sensitive use cases that need to reduce token usage while trading off intelligence.
* **`low`:** Reserve for short, scoped tasks and latency-sensitive workloads that are not intelligence-sensitive.

As a rough cross-model mapping when migrating: Claude Sonnet 5 at medium is comparable in intelligence to Claude Sonnet 4.6 at high, and Claude Sonnet 5 at high is comparable to Claude Sonnet 4.6 at max. When benchmarking, match by observed thinking length rather than effort name.

Claude Sonnet 5 respects effort levels strictly, especially at the low end. At `low` and `medium`, the model scopes its work to what was asked rather than going above and beyond. This is good for latency and cost, but on moderately complex tasks running at `low` effort there is some risk of under-thinking.

If you observe shallow reasoning on complex problems, raise effort to `high` or `xhigh` rather than prompting around it. If you need to keep effort at `low` for latency, add targeted guidance:

```text wrap
This task involves multi-step reasoning. Think carefully through the problem before responding.
```

On Claude Sonnet 5, [adaptive thinking](/docs/en/build-with-claude/adaptive-thinking) is on by default. Requests without a `thinking` field run with adaptive thinking. This is a change from Claude Sonnet 4.6, where the same requests ran without thinking. To turn thinking off entirely, pass `thinking: {type: "disabled"}`. Because `max_tokens` is a hard limit on total output (thinking plus response text), revisit it for workloads that ran without thinking on Claude Sonnet 4.6. If you were previously using thinking off with Claude Sonnet 4.6, try thinking on with lower effort levels for Claude Sonnet 5.

The triggering behavior for adaptive thinking is steerable. If you find the model emitting thinking blocks more often than you'd like, which can happen with large or complex system prompts, add guidance to steer it. As always, measure the effect of any prompting changes on performance. Example:

```text wrap
Thinking adds latency and should only be used when it will meaningfully improve answer quality, typically for problems that require multi-step reasoning. When in doubt, respond directly.
```

Conversely, if you're running hard workloads at `medium` and seeing under-thinking, the first lever is to raise effort. If you need finer control, prompt for it directly.

Manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) is not supported on Claude Sonnet 5 and returns a 400 error. It was deprecated on Claude Sonnet 4.6 and is now removed. Use adaptive thinking with the effort parameter instead.

<Note>
  If you are running Claude Sonnet 5 at `high`, `xhigh`, or `max` effort, leave headroom in `max_tokens` so the model has room for thinking and tool calls. On long tasks, adaptive thinking can use a large share of the budget; if the budget is tight, you may see a response that is almost entirely thinking followed by a truncated answer and `stop_reason: "max_tokens"`. Raising `max_tokens` or dropping to `medium` effort resolves this. Because Claude Sonnet 5 uses a [new tokenizer](/docs/en/about-claude/models/whats-new-sonnet-5#new-tokenizer) that produces approximately 30% more tokens for the same text, `max_tokens` limits tuned for Claude Sonnet 4.6 may truncate equivalent output. The exact increase depends on the content and workload shape.
</Note>

## Tool use triggering

Claude Sonnet 5 is more agentic than Claude Sonnet 4.6 by default and will reach for tools and run self-verification loops more readily. With thinking disabled, the model is less likely to reach for tools or consider searching; if you rely on tool calls with thinking off, add an explicit nudge in the system prompt. Effort is also a lever for tool usage: `high` or `xhigh` effort settings show substantially more tool usage in agentic search and coding. For scenarios where you want more tool use, you can also adjust your prompt to explicitly instruct the model about when and how to properly use its tools. For instance, if you find that the model is not using your web search tools, clearly describe why and how it should.

## User-facing progress updates

Claude Sonnet 5 provides regular, higher-quality updates to the user throughout long agentic traces. If you've added scaffolding to force interim status messages ("After every 3 tool calls, summarize progress"), try removing it. If you find that the length or contents of Claude Sonnet 5's user-facing updates are not well-calibrated to your use case, explicitly describe what these updates should look like in the prompt and provide examples.

## More literal instruction following

Claude Sonnet 5 interprets prompts literally and explicitly, particularly at lower effort levels. It does not silently generalize an instruction from one item to another, and it does not infer requests you didn't make. The upside of this literalism is precision, and it generally performs better for API use cases with carefully tuned prompts, structured extraction, and pipelines where you want predictable behavior. If you need Claude to apply an instruction broadly, state the scope explicitly (for example, "Apply this formatting to every section, not just the first one").

## Tone and writing style

As with any new model, prose style on long-form writing may shift. If your product relies on a specific voice, re-evaluate style prompts against the new baseline.

For instance, if your product voice is warmer or more conversational, add:

```text wrap
Use a warm, collaborative tone. Acknowledge the user's framing before answering.
```

If you previously relied on `temperature` for stylistic variety, note that setting `temperature`, `top_p`, or `top_k` to a non-default value returns a 400 error on Claude Sonnet 5. This constraint is new for Sonnet-class models. Remove these parameters when migrating, and use system-prompt instructions to guide tone and variety instead.

## Design and frontend defaults

Claude Sonnet 5 may settle into a consistent default visual style on open-ended frontend and design briefs. A default house style can read well for some briefs but feel off for dashboards, dev tools, fintech, healthcare, or enterprise apps.

Generic instructions ("don't use that color," "make it clean and minimal") tend to shift the model to a different fixed palette rather than producing variety. Two approaches work reliably:

**1. Specify a concrete alternative.** The model follows explicit specs precisely:

```text wrap
Design a desktop landing page for a supplement brand called AEFRM.

The visual direction should come from a cold monochrome atmosphere using pale silver-gray tones that gradually deepen into blue-gray and near-black, similar to a misted metallic surface.

The page should feel sharp and controlled, with a strong sense of structure and restraint.

Use this tonal system across the full page instead of introducing bright accent colors.

Use the uploaded image on the hero design in black and white.

The layout should be built with clear horizontal sections and a centered max-width container. Use 4px corner radius consistently across cards, buttons, inputs, and media frames. Margins should feel generous, with enough empty space around each section so the page breathes.

Typography should use a square, angular sans-serif with wider letter spacing than usual, especially in headings and navigation, so the text feels more engineered and less compressed. Headline text can be large and uppercase, while supporting copy remains short and sparse. The sub texts should be written with Alumni Sans SC in 4-6px like tiny little texts on corners bottom centre like that.

For the structure, start with a hero section containing a strong product statement, one short supporting paragraph, and a clean product placeholder or packshot frame. Below that, add a benefit grid with three or four blocks, then a formulation or ingredients section, and finally a cta.

Buttons should be flat and precise, with subtle hover changes using transition: all 160ms ease out where brightness and border contrast shift slightly rather than using dramatic motion.

Color palette should stay within this range:
#E9ECEC, #C9D2D4, #8C9A9E, #44545B, #11171B.
```

**2. Have the model propose options before building.** This breaks the default and gives users control. Because `temperature` is not accepted on Claude Sonnet 5, this approach is the recommended way to produce meaningfully different design directions across runs. Example prompt:

```text wrap
Before building, propose 4 distinct visual directions tailored to this brief (each as: bg hex / accent hex / typeface, plus a one-line rationale). Ask the user to pick one, then implement only that direction.
```

To steer away from generic patterns that users call the "AI slop" aesthetic, you can include a short directive in your system prompt. The [frontend-design skill](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md) provides a fuller treatment, but this snippet works well alongside the preceding variety approaches:

```text wrap
<frontend_aesthetics>
NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white or dark backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character. Use unique fonts, cohesive colors and themes, and animations for effects and micro-interactions.
</frontend_aesthetics>
```

## Interactive coding products

Token usage and behavior can differ between autonomous, asynchronous coding agents with a single user turn and interactive, synchronous coding agents with multiple user turns. To maximize both performance and token efficiency in coding products, use `xhigh` or `high` effort, add autonomous features like an auto mode, and reduce the number of human interactions required from your users.

When limiting the number of required user interactions, it's important to specify the task, intent, and relevant constraints upfront in the first human turn. Providing well-specified, clear, and accurate task descriptions upfront can help maximize autonomy and intelligence while minimizing extra token usage after user turns. In contrast, ambiguous or underspecified prompts conveyed progressively over multiple user turns tend to relatively reduce token efficiency and sometimes performance.

## Code review harnesses

If your code-review harness was tuned for an earlier model, you may initially see lower recall on Claude Sonnet 5. This is likely a harness effect, not a capability regression. When a review prompt says things like "only report high-severity issues," "be conservative," or "don't nitpick," Claude Sonnet 5 may follow that instruction more faithfully than earlier models did: it may investigate the code just as thoroughly, identify the bugs, and then not report findings it judges to be below your stated bar. This can show up as the model doing the same depth of investigation but converting fewer investigations into reported findings, especially on lower-severity bugs. Precision typically rises, but measured recall can fall even though the model's underlying bug-finding ability has improved.

Some recommended prompt language:

```text wrap
Report every issue you find, including ones you are uncertain about or consider low-severity. Do not filter for importance or confidence at this stage - a separate verification step will do that. Your goal here is coverage: it is better to surface a finding that later gets filtered out than to silently drop a real bug. For each finding, include your confidence level and an estimated severity so a downstream filter can rank them.
```

This prompt can be used without having an actual second step, but moving confidence filtering out of the finding step often helps. If your harness has a separate verification, deduplication, or ranking stage, tell the model explicitly that its job at the finding stage is coverage rather than filtering.

If you do want the model to self-filter in a single pass, be concrete about where the bar is rather than using qualitative terms like "important": for example, "report any bugs that could cause incorrect behavior, a test failure, or a misleading result; only omit nits like pure style or naming preferences."

Iterate on prompts against a subset of your evals or test cases to validate recall or F1 score gains.

## Computer use

Claude Sonnet 5 supports the `computer_20251124` tool version. [Computer use](/docs/en/agents-and-tools/tool-use/computer-use-tool) capability works across resolutions, up to a maximum resolution of 2576px / 3.75MP. Internal computer use testing shows that sending images at 1080p provides a good balance of performance and cost.

For particularly cost-sensitive workloads, 720p or 1366×768 are lower-cost options with strong performance. Conduct your own testing to find the ideal settings for your use case; experimenting with effort settings can also help tune the model's behavior.



# https://platform.claude.com/docs/en/test-and-evaluate/define-success.md

# Define success criteria and build evaluations

---

Building a successful LLM-based application starts with clearly defining your success criteria and then designing evaluations to measure performance against them. This cycle is central to prompt engineering.

![Flowchart of prompt engineering: test cases, preliminary prompt, iterative testing and refinement, final validation, ship](/docs/images/how-to-prompt-eng.png)

## Define your success criteria

Good success criteria are:

* **Specific:** Clearly define what you want to achieve. Instead of "good performance," specify "accurate sentiment classification."

* **Measurable:** Use quantitative metrics or well-defined qualitative scales. Numbers provide clarity and scalability, but qualitative measures can be valuable if consistently applied *along* with quantitative measures.

  * Even "hazy" topics such as ethics and safety can be quantified:

    |      | Safety criteria                                                                            |
    | ---- | ------------------------------------------------------------------------------------------ |
    | Bad  | Safe outputs                                                                               |
    | Good | Less than 0.1% of outputs out of 10,000 trials flagged for toxicity by our content filter. |

  <Accordion title="Example metrics and measurement methods">
    **Quantitative metrics:**

    * Task-specific: F1 score, BLEU score, perplexity
    * Generic: Accuracy, precision, recall
    * Operational: Response time (ms), uptime (%)

    **Quantitative methods:**

    * A/B testing: Compare performance against a baseline model or earlier version.
    * User feedback: Implicit measures like task completion rates.
    * Edge case analysis: Percentage of edge cases handled without errors.

    **Qualitative scales:**

    * Likert scales: "Rate coherence from 1 (nonsensical) to 5 (perfectly logical)"
    * Expert rubrics: Linguists rating translation quality on defined criteria
  </Accordion>

* **Achievable:** Base your targets on industry benchmarks, prior experiments, AI research, or expert knowledge. Your success metrics should not be unrealistic to current frontier model capabilities.

* **Relevant:** Align your criteria with your application's purpose and user needs. Strong citation accuracy might be critical for medical apps but less so for casual chatbots.

<Accordion title="Example task fidelity criteria for sentiment analysis">
  |      | Criteria                                                                                                                                                                                                                               |
  | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Bad  | The model should classify sentiments well                                                                                                                                                                                              |
  | Good | Our sentiment analysis model should achieve an F1 score of at least 0.85 (Measurable, Specific) on a held-out test set\* of 10,000 diverse Twitter posts (Relevant), which is a 5% improvement over our current baseline (Achievable). |

  \*More on held-out test sets in the next section.
</Accordion>

### Common success criteria

Here are some criteria that might be important for your use case. This list is non-exhaustive.

<AccordionGroup>
  <Accordion title="Task fidelity">
    How well does the model need to perform on the task? You may also need to consider edge case handling, such as how well the model needs to perform on rare or challenging inputs.
  </Accordion>

  <Accordion title="Consistency">
    How similar does the model's responses need to be for similar types of input? If a user asks the same question twice, how important is it that they get semantically similar answers?
  </Accordion>

  <Accordion title="Relevance and coherence">
    How well does the model directly address the user's questions or instructions? How important is it for the information to be presented in a logical, easy to follow manner?
  </Accordion>

  <Accordion title="Tone and style">
    How well does the model's output style match expectations? How appropriate is its language for the target audience?
  </Accordion>

  <Accordion title="Privacy preservation">
    What is a successful metric for how the model handles personal or sensitive information? Can it follow instructions not to use or share certain details?
  </Accordion>

  <Accordion title="Context utilization">
    How effectively does the model use provided context? How well does it reference and build upon information given in its history?
  </Accordion>

  <Accordion title="Latency">
    What is the acceptable response time for the model? This will depend on your application's real-time requirements and user expectations.
  </Accordion>

  <Accordion title="Price">
    What is your budget for running the model? Consider factors like the cost per API call, the size of the model, and the frequency of usage.
  </Accordion>
</AccordionGroup>

Most use cases will need multidimensional evaluation along several success criteria.

<Accordion title="Example multidimensional criteria for sentiment analysis">
  |      | Criteria                                                                                                                                                                                                                                                               |
  | ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Bad  | The model should classify sentiments well                                                                                                                                                                                                                              |
  | Good | On a held-out test set of 10,000 diverse Twitter posts, our sentiment analysis model should achieve: - an F1 score of at least 0.85 - 99.5% of outputs are non-toxic - 90% of errors are would cause inconvenience, not egregious error\* - 95% response time \< 200ms |

  \*In reality, we would also define what "inconvenience" and "egregious" means.
</Accordion>

***

## Build evaluations

### Eval design principles

1. **Be task-specific:** Design evals that mirror your real-world task distribution. Don't forget to factor in edge cases!
   <Accordion title="Example edge cases">
     * Irrelevant or nonexistent input data
     * Overly long input data or user input
     * \[Chat use cases] Poor, harmful, or irrelevant user input
     * Ambiguous test cases where even humans would find it hard to reach an assessment consensus
   </Accordion>
2. **Automate when possible:** Structure questions to allow for automated grading (e.g., multiple-choice, string match, code-graded, LLM-graded).
3. **Prioritize volume over quality:** More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals.

### Example evals

<AccordionGroup>
  <Accordion title="Task fidelity (sentiment analysis) - exact match evaluation">
    **What it measures**: Exact match evals measure whether the model's output matches a predefined correct answer, typically after normalizing whitespace and case. It's a simple, unambiguous metric that's perfect for tasks with clear-cut, categorical answers like sentiment analysis (positive, negative, neutral).

    **Example eval test cases**: 1000 tweets with human-labeled sentiments.

    ```python
    import anthropic

    tweets = [
        {"text": "This movie was a total waste of time. 👎", "sentiment": "negative"},
        {"text": "The new album is 🔥! Been on repeat all day.", "sentiment": "positive"},
        {
            "text": "I just love it when my flight gets delayed for 5 hours. #bestdayever",
            "sentiment": "negative",
        },  # Edge case: Sarcasm
        {
            "text": "The movie's plot was terrible, but the acting was phenomenal.",
            "sentiment": "mixed",
        },  # Edge case: Mixed sentiment
        # ... 996 more tweets
    ]

    client = anthropic.Anthropic()


    def get_completion(prompt: str):
        message = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=50,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text


    def evaluate_exact_match(model_output, correct_answer):
        return model_output.strip().lower() == correct_answer.lower()


    outputs = [
        get_completion(
            f"Classify this as 'positive', 'negative', 'neutral', or 'mixed': {tweet['text']}"
        )
        for tweet in tweets
    ]
    accuracy = sum(
        evaluate_exact_match(output, tweet["sentiment"])
        for output, tweet in zip(outputs, tweets)
    ) / len(tweets)
    print(f"Sentiment Analysis Accuracy: {accuracy * 100}%")
    ```
  </Accordion>

  <Accordion title="Consistency (FAQ bot) - cosine similarity evaluation">
    **What it measures**: Cosine similarity measures the similarity between two vectors (in this case, sentence embeddings of the model's output using [Sentence-BERT (SBERT)](https://sbert.net/)) by computing the cosine of the angle between them. Values closer to 1 indicate higher similarity. It's ideal for evaluating consistency because similar questions should yield semantically similar answers, even if the wording varies.

    **Example eval test cases**: 50 groups with a few paraphrased versions each.

    ```python
    from sentence_transformers import SentenceTransformer
    import numpy as np
    import anthropic

    faq_variations = [
        {
            "questions": [
                "What's your return policy?",
                "How can I return an item?",
                "Wut's yur retrn polcy?",
            ],
            "answer": "Our return policy allows...",
        },  # Edge case: Typos
        {
            "questions": [
                "I bought something last week, and it's not really what I expected, so I was wondering if maybe I could possibly return it?",
                "I read online that your policy is 30 days but that seems like it might be out of date because the website was updated six months ago, so I'm wondering what exactly is your current policy?",
            ],
            "answer": "Our return policy allows...",
        },  # Edge case: Long, rambling question
        {
            "questions": [
                "I'm Jane's cousin, and she said you guys have great customer service. Can I return this?",
                "Reddit told me that contacting customer service this way was the fastest way to get an answer. I hope they're right! What is the return window for a jacket?",
            ],
            "answer": "Our return policy allows...",
        },  # Edge case: Irrelevant info
        # ... 47 more FAQs
    ]

    client = anthropic.Anthropic()


    def get_completion(prompt: str):
        message = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text


    def evaluate_cosine_similarity(outputs):
        model = SentenceTransformer("all-MiniLM-L6-v2")
        embeddings = model.encode(outputs)

        norms = np.linalg.norm(embeddings, axis=1)
        cosine_similarities = np.dot(embeddings, embeddings.T) / np.outer(norms, norms)
        return np.mean(cosine_similarities)


    for faq in faq_variations:
        outputs = [get_completion(question) for question in faq["questions"]]
        similarity_score = evaluate_cosine_similarity(outputs)
        print(f"FAQ Consistency Score: {similarity_score * 100}%")
    ```
  </Accordion>

  <Accordion title="Relevance and coherence (summarization) - ROUGE-L evaluation">
    **What it measures**: ROUGE-L (Recall-Oriented Understudy for Gisting Evaluation - Longest Common Subsequence) evaluates the quality of generated summaries. It measures the length of the longest common subsequence between the candidate and reference summaries. High ROUGE-L scores indicate that the generated summary captures key information in a coherent order.

    **Example eval test cases**: 200 articles with reference summaries.

    ```python
    from rouge import Rouge
    import anthropic

    articles = [
        {
            "text": "In a groundbreaking study, researchers at MIT...",
            "summary": "MIT scientists discover a new antibiotic...",
        },
        {
            "text": "Jane Doe, a local hero, made headlines last week for saving... In city hall news, the budget... Meteorologists predict...",
            "summary": "Community celebrates local hero Jane Doe while city grapples with budget issues.",
        },  # Edge case: Multi-topic
        {
            "text": "You won't believe what this celebrity did! ... extensive charity work ...",
            "summary": "Celebrity's extensive charity work surprises fans",
        },  # Edge case: Misleading title
        # ... 197 more articles
    ]

    client = anthropic.Anthropic()


    def get_completion(prompt: str):
        message = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text


    def evaluate_rouge_l(model_output, true_summary):
        rouge = Rouge()
        scores = rouge.get_scores(model_output, true_summary)
        return scores[0]["rouge-l"]["f"]  # ROUGE-L F1 score


    outputs = [
        get_completion(f"Summarize this article in 1-2 sentences:\n\n{article['text']}")
        for article in articles
    ]
    relevance_scores = [
        evaluate_rouge_l(output, article["summary"])
        for output, article in zip(outputs, articles)
    ]
    print(f"Average ROUGE-L F1 Score: {sum(relevance_scores) / len(relevance_scores)}")
    ```
  </Accordion>

  <Accordion title="Tone and style (customer service) - LLM-based Likert scale">
    **What it measures**: The LLM-based Likert scale is a psychometric scale that uses an LLM to judge subjective attitudes or perceptions. Here, it's used to rate the tone of responses on a scale from 1 to 5. It's ideal for evaluating nuanced aspects like empathy, professionalism, or patience that are difficult to quantify with traditional metrics.

    **Example eval test cases**: 100 customer inquiries with target tone (empathetic, patient, professional).

    ```python
    import anthropic

    inquiries = [
        {
            "text": "This is the third time you've messed up my order. I want a refund NOW!",
            "tone": "empathetic",
        },  # Edge case: Angry customer
        {
            "text": "I tried resetting my password but then my account got locked...",
            "tone": "patient",
        },  # Edge case: Complex issue
        {
            "text": "I can't believe how good your product is. It's ruined all others for me!",
            "tone": "professional",
        },  # Edge case: Compliment as complaint
        # ... 97 more inquiries
    ]

    client = anthropic.Anthropic()


    def get_completion(prompt: str):
        message = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text


    def evaluate_likert(model_output, target_tone):
        tone_prompt = f"""Rate this customer service response on a scale of 1-5 for being {target_tone}:
        <response>{model_output}</response>
        1: Not at all {target_tone}
        5: Perfectly {target_tone}
        Output only the number."""

        # Generally best practice to use a different model to evaluate than the model used to generate the evaluated output
        response = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=50,
            messages=[{"role": "user", "content": tone_prompt}],
        )
        return int(response.content[0].text.strip())


    outputs = [
        get_completion(f"Respond to this customer inquiry: {inquiry['text']}")
        for inquiry in inquiries
    ]
    tone_scores = [
        evaluate_likert(output, inquiry["tone"])
        for output, inquiry in zip(outputs, inquiries)
    ]
    print(f"Average Tone Score: {sum(tone_scores) / len(tone_scores)}")
    ```
  </Accordion>

  <Accordion title="Privacy preservation (medical chatbot) - LLM-based binary classification">
    **What it measures**: Binary classification determines if an input belongs to one of two classes. Here, it's used to classify whether a response contains PHI or not. This method can understand context and identify subtle or implicit forms of PHI that rule-based systems might miss.

    **Example eval test cases**: 500 simulated patient queries, some with PHI.

    ```python
    import anthropic

    patient_queries = [
        {"query": "What are the side effects of Lisinopril?", "contains_phi": False},
        {
            "query": "Can you tell me why John Doe, DOB 5/12/1980, was prescribed Metformin?",
            "contains_phi": True,
        },  # Edge case: Explicit PHI
        {
            "query": "If my friend Alice, who was born on July 4, 1985, had diabetes, what...",
            "contains_phi": True,
        },  # Edge case: Hypothetical PHI
        {
            "query": "I'm worried about my son. He's been prescribed the same medication as his father last year.",
            "contains_phi": True,
        },  # Edge case: Implicit PHI
        # ... 496 more queries
    ]

    client = anthropic.Anthropic()


    def get_completion(prompt: str):
        message = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text


    def evaluate_binary(model_output, query_contains_phi):
        if not query_contains_phi:
            return True

        binary_prompt = f"""Does this response contain or reference any Personal Health Information (PHI)?
        PHI refers to any individually identifiable health data that is created, used, or disclosed in the course of providing healthcare services. This includes information related to an individual's physical or mental health condition, the provision of healthcare to that individual, or payment for such care.
        Key aspects of PHI include:
        - Identifiers: Names, addresses, birthdates, Social Security numbers, medical record numbers, etc.
        - Health data: Diagnoses, treatment plans, test results, medication records, etc.
        - Financial information: Insurance details, payment records, etc.
        - Communication: Notes from healthcare providers, emails or messages about health.

        <response>{model_output}</response>
        Output only 'yes' or 'no'."""

        # Generally best practice to use a different model to evaluate than the model used to generate the evaluated output
        response = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=50,
            messages=[{"role": "user", "content": binary_prompt}],
        )
        return response.content[0].text.strip().lower() == "no"


    outputs = [
        get_completion(
            f"You are a


# https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md

# Agent Skills

Agent Skills are modular capabilities that extend Claude's functionality. Each Skill packages instructions, metadata, and optional resources (scripts, templates) that Claude uses automatically when relevant.

---

<Note>
  This feature is **not** eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/api-and-data-retention). Data is retained according to the feature's standard retention policy.
</Note>

## Why use Skills

Skills are reusable, filesystem-based resources that provide Claude with domain-specific expertise: workflows, context, and best practices that transform general-purpose agents into specialists. Unlike prompts (conversation-level instructions for one-off tasks), Skills load on-demand and eliminate the need to repeatedly provide the same guidance across multiple conversations.

**Key benefits**:

* **Specialize Claude**: Tailor capabilities for domain-specific tasks
* **Reduce repetition**: Create once, use automatically
* **Compose capabilities**: Combine Skills to build complex workflows

<Note>
  For a deep dive into the architecture and real-world applications of Agent Skills, see the engineering blog post [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).
</Note>

## Using Skills

Anthropic provides pre-built Agent Skills for common document tasks (PowerPoint, Excel, Word, PDF), and you can create your own custom Skills. Both work the same way. Claude automatically uses them when relevant to your request.

**Pre-built Agent Skills** are available on claude.ai, the Claude API, [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws), and [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry). On Microsoft Foundry, Agent Skills require a [Hosted on Anthropic deployment](/docs/en/build-with-claude/claude-in-microsoft-foundry#additional-features-not-supported-when-hosted-on-azure). See [Available Skills](#available-skills) for the complete list.

**Custom Skills** let you package domain expertise and organizational knowledge. They're available across Claude's products: create them in Claude Code, upload them through the Claude API, or add them in claude.ai settings. On [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws) and [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry), upload custom Skills through the Skills API.

<Note>
  **Get started:**

  * For pre-built Agent Skills: See the [quickstart tutorial](/docs/en/agents-and-tools/agent-skills/quickstart) to start using PowerPoint, Excel, Word, and PDF skills in the API
  * For custom Skills: See the [Agent Skills Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction) to learn how to create your own Skills
</Note>

## How Skills work

Skills leverage Claude's VM environment to provide capabilities beyond what's possible with prompts alone. Claude operates in a virtual machine with filesystem access, allowing Skills to exist as directories containing instructions, executable code, and reference materials, organized like an onboarding guide you'd create for a new team member.

This filesystem-based architecture enables **progressive disclosure**: Claude loads information in stages as needed, rather than consuming context upfront.

### Three types of Skill content, three levels of loading

Skills can contain three types of content, each loaded at different times:

### Level 1: Metadata (always loaded)

**Content type: Instructions**. The Skill's YAML frontmatter provides discovery information:

```yaml
---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---
```

Claude loads this metadata at startup and includes it in the system prompt. This lightweight approach means you can install many Skills without context penalty; Claude only knows each Skill exists and when to use it.

### Level 2: Instructions (loaded when triggered)

**Content type: Instructions**. The main body of SKILL.md contains procedural knowledge: workflows, best practices, and guidance:

````markdown
# PDF Processing

## Quick start

Use pdfplumber to extract text from PDFs:

```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

For advanced form filling, see [FORMS.md](FORMS.md).
````

When you request something that matches a Skill's description, Claude reads SKILL.md from the filesystem via bash. Only then does this content enter the context window.

### Level 3: Resources and code (loaded as needed)

**Content types: Instructions, code, and resources**. Skills can bundle additional materials:

```text
pdf-skill/
├── SKILL.md (main instructions)
├── FORMS.md (form-filling guide)
├── REFERENCE.md (detailed API reference)
└── scripts/
    └── fill_form.py (utility script)
```

**Instructions**: Additional markdown files (FORMS.md, REFERENCE.md) containing specialized guidance and workflows

**Code**: Executable scripts (fill\_form.py, validate.py) that Claude runs via bash; scripts provide deterministic operations without consuming context

**Resources**: Reference materials like database schemas, API documentation, templates, or examples

Claude accesses these files only when referenced. The filesystem model means each content type has different strengths: instructions for flexible guidance, code for reliability, resources for factual lookup.

| Level                     | When Loaded             | Token Cost             | Content                                                               |
| ------------------------- | ----------------------- | ---------------------- | --------------------------------------------------------------------- |
| **Level 1: Metadata**     | Always (at startup)     | \~100 tokens per Skill | `name` and `description` from YAML frontmatter                        |
| **Level 2: Instructions** | When Skill is triggered | Under 5k tokens        | SKILL.md body with instructions and guidance                          |
| **Level 3+: Resources**   | As needed               | Effectively unlimited  | Bundled files executed via bash without loading contents into context |

Progressive disclosure ensures only relevant content occupies the context window at any given time.

### The Skills architecture

Skills run in a code execution environment where Claude has filesystem access, bash commands, and code execution capabilities. Think of it like this: Skills exist as directories on a virtual machine, and Claude interacts with them using the same bash commands you'd use to navigate files on your computer.

![Agent Skills Architecture - showing how Skills integrate with the agent's configuration and virtual machine](/docs/images/agent-skills-architecture.png)

**How Claude accesses Skill content:**

When a Skill is triggered, Claude uses bash to read SKILL.md from the filesystem, bringing its instructions into the context window. If those instructions reference other files (like FORMS.md or a database schema), Claude reads those files too using additional bash commands. When instructions mention executable scripts, Claude runs them via bash and receives only the output (the script code itself never enters context).

**What this architecture enables:**

**On-demand file access**: Claude reads only the files needed for each specific task. A Skill can include dozens of reference files, but if your task only needs the sales schema, Claude loads just that one file. The rest remain on the filesystem consuming zero tokens.

**Efficient script execution**: When Claude runs `validate_form.py`, the script's code never loads into the context window. Only the script's output (like "Validation passed" or specific error messages) consumes tokens. This makes scripts far more efficient than having Claude generate equivalent code on the fly.

**No practical limit on bundled content**: Because files don't consume context until accessed, Skills can include comprehensive API documentation, large datasets, extensive examples, or any reference materials you need. There's no context penalty for bundled content that isn't used.

This filesystem-based model is what makes progressive disclosure work. Claude navigates your Skill like you'd reference specific sections of an onboarding guide, accessing exactly what each task requires.

### Example: Loading a PDF processing skill

Here's how Claude loads and uses a PDF processing skill:

1. **Startup**: System prompt includes: `PDF Processing - Extract text and tables from PDF files, fill forms, merge documents`
2. **User request**: "Extract the text from this PDF and summarize it"
3. **Claude invokes**: `bash: read pdf-skill/SKILL.md` → Instructions loaded into context
4. **Claude determines**: Form filling is not needed, so FORMS.md is not read
5. **Claude executes**: Uses instructions from SKILL.md to complete the task

![Skills loading into context window - showing the progressive loading of skill metadata and content](/docs/images/agent-skills-context-window.png)

The diagram shows:

1. Default state with system prompt and skill metadata pre-loaded
2. Claude triggers the skill by reading SKILL.md via bash
3. Claude optionally reads additional bundled files like FORMS.md as needed
4. Claude proceeds with the task

This dynamic loading ensures only relevant skill content occupies the context window.

## Where Skills work

Skills are available across Claude's agent products:

<Note>
  Claude Platform on AWS and Microsoft Foundry inherit the same Skills behavior as the Claude API in all following sections.
</Note>

### Claude API

The Claude API supports both pre-built Agent Skills and custom Skills. Both work identically: specify the relevant `skill_id` in the `container` parameter along with the code execution tool.

**Prerequisites**: Using Skills via the API requires three beta headers:

* `code-execution-2025-08-25` - Skills run in the code execution container
* `skills-2025-10-02` - Enables Skills functionality
* `files-api-2025-04-14` - Required for uploading/downloading files to/from the container

Use pre-built Agent Skills by referencing their `skill_id` (for example, `pptx`, `xlsx`), or create and upload your own through the Skills API (`/v1/skills` endpoints). Custom Skills are shared workspace-wide; all workspace members can access them.

To learn more, see [Use Skills with the Claude API](/docs/en/build-with-claude/skills-guide).

### Claude Code

[Claude Code](https://code.claude.com/docs/en/overview) supports only Custom Skills.

**Custom Skills**: Create Skills as directories with SKILL.md files. Claude discovers and uses them automatically.

Custom Skills in Claude Code are filesystem-based and don't require API uploads.

To learn more, see [Use Skills in Claude Code](https://code.claude.com/docs/en/skills).

### claude.ai

[claude.ai](https://claude.ai) supports both pre-built Agent Skills and custom Skills.

**Pre-built Agent Skills**: These Skills are already working behind the scenes when you create documents. Claude uses them without requiring any setup.

**Custom Skills**: Upload your own Skills as zip files through Settings > Features. Available on Pro, Max, Team, and Enterprise plans with code execution enabled. Custom Skills are individual to each user; they are not shared organization-wide and cannot be centrally managed by admins.

To learn more about using Skills in claude.ai, see the following resources in the Claude Help Center:

* [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
* [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
* [How to create custom Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
* [Teach Claude your way of working using Skills](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills)

## Skill structure

Every Skill requires a `SKILL.md` file with YAML frontmatter:

```yaml
---
name: your-skill-name
description: Brief description of what this Skill does and when to use it
---

# Your Skill Name

## Instructions
[Clear, step-by-step guidance for Claude to follow]

## Examples
[Concrete examples of using this Skill]
```

**Required fields**: `name` and `description`

**Field requirements**:

`name`:

* Maximum 64 characters
* Must contain only lowercase letters, numbers, and hyphens
* Cannot contain XML tags
* Cannot contain reserved words: "anthropic", "claude"

`description`:

* Must be non-empty
* Maximum 1024 characters
* Cannot contain XML tags

The `description` should include both what the Skill does and when Claude should use it. For complete authoring guidance, see the [best practices guide](/docs/en/agents-and-tools/agent-skills/best-practices).

## Security considerations

Use Skills only from trusted sources: those you created yourself or obtained from Anthropic. Skills provide Claude with new capabilities through instructions and code, and while this makes them powerful, it also means a malicious Skill can direct Claude to invoke tools or execute code in ways that don't match the Skill's stated purpose.

<Warning>
  If you must use a Skill from an untrusted or unknown source, exercise extreme caution and thoroughly audit it before use. Depending on what access Claude has when executing the Skill, malicious Skills could lead to data exfiltration, unauthorized system access, or other security risks.
</Warning>

**Key security considerations**:

* **Audit thoroughly**: Review all files bundled in the Skill: SKILL.md, scripts, images, and other resources. Look for unusual patterns like unexpected network calls, file access patterns, or operations that don't match the Skill's stated purpose
* **External sources are risky**: Skills that fetch data from external URLs pose particular risk, as fetched content may contain malicious instructions. Even trustworthy Skills can be compromised if their external dependencies change over time
* **Tool misuse**: Malicious Skills can invoke tools (file operations, bash commands, code execution) in harmful ways
* **Data exposure**: Skills with access to sensitive data could be designed to leak information to external systems
* **Treat like installing software**: Only use Skills from trusted sources. Be especially careful when integrating Skills into production systems with access to sensitive data or critical operations

## Available Skills

### Pre-built Agent Skills

The following pre-built Agent Skills are available for immediate use:

* **PowerPoint (pptx)**: Create presentations, edit slides, analyze presentation content
* **Excel (xlsx)**: Create spreadsheets, analyze data, generate reports with charts
* **Word (docx)**: Create documents, edit content, format text
* **PDF (pdf)**: Generate formatted PDF documents and reports

These Skills are available on the Claude API, [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws), [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry), and claude.ai. On Microsoft Foundry, Agent Skills require a [Hosted on Anthropic deployment](/docs/en/build-with-claude/claude-in-microsoft-foundry#additional-features-not-supported-when-hosted-on-azure). See the [quickstart tutorial](/docs/en/agents-and-tools/agent-skills/quickstart) to start using them in the API.

### Open-source Skills

Anthropic also publishes open-source Skills in the [skills repository](https://github.com/anthropics/skills):

* **[Claude API](/docs/en/agents-and-tools/agent-skills/claude-api-skill)**: Provides Claude with up-to-date API reference material, SDK documentation, and best practices for 8 programming languages. Bundled with Claude Code and also available for installation from the skills repository.

### Custom Skills examples

For complete examples of custom Skills, see the [Skills cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction).

## Data retention

Agent Skills is not covered by ZDR arrangements. Skill definitions and execution data are retained according to Anthropic's standard data retention policy.

For ZDR eligibility across all features, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).

## Limitations and constraints

Understanding these limitations helps you plan your Skills deployment effectively. Claude Platform on AWS and Microsoft Foundry follow the same limitations as the Claude API in the following subsections.

### Cross-surface availability

**Custom Skills do not sync across surfaces**. Skills uploaded to one surface are not automatically available on others:

* Skills uploaded to claude.ai must be separately uploaded to the API
* Skills uploaded through the API are not available on claude.ai
* Claude Code Skills are filesystem-based and separate from both claude.ai and API

You'll need to manage and upload Skills separately for each surface where you want to use them.

### Sharing scope

Skills have different sharing models depending on where you use them:

* **claude.ai**: Individual user only; each team member must upload separately
* **Claude API**: Workspace-wide; all workspace members can access uploaded Skills
* **Claude Code**: Personal (`~/.claude/skills/`) or project-based (`.claude/skills/`); can also be shared via Claude Code Plugins

claude.ai does not support centralized admin management or org-wide distribution of custom Skills.

### Runtime environment constraints

The exact runtime environment available to your skill depends on the product surface where you use it.

* **claude.ai**:
  * **Varying network access**: Depending on user/admin settings, Skills may have full, partial, or no network access. For more details, see the [Create and Edit Files](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_6b7e833898) support article.

* **Claude API**:

  * **No network access**: Skills cannot make external API calls or access the internet
  * **No runtime package installation**: Only pre-installed packages are available. You cannot install new packages during execution.
  * **Pre-configured dependencies only**: Check the [code execution tool documentation](/docs/en/agents-and-tools/tool-use/code-execution-tool) for the list of available packages

* **Claude Code**:

  * **Full network access**: Skills have the same network access as any other program on the user's computer
  * **Global package installation discouraged**: Skills should only install packages locally in order to avoid interfering with the user's computer

Plan your Skills to work within these constraints.

## Next steps

<CardGroup cols={2}>
  <Card title="Get started with Agent Skills" icon="graduation-cap" href="/docs/en/agents-and-tools/agent-skills/quickstart">
    Create your first Skill
  </Card>

  <Card title="API Guide" icon="code" href="/docs/en/build-with-claude/skills-guide">
    Use Skills with the Claude API
  </Card>

  <Card title="Use Skills in Claude Code" icon="terminal" href="https://code.claude.com/docs/en/skills">
    Create and manage custom Skills in Claude Code
  </Card>

  <Card title="Authoring best practices" icon="lightbulb" href="/docs/en/agents-and-tools/agent-skills/best-practices">
    Write Skills that Claude can use effectively
  </Card>
</CardGroup>



# https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md

# Skill authoring best practices

Learn how to write effective Skills that Claude can discover and use successfully.

---

Good Skills are concise, well-structured, and tested with real usage. This guide provides practical authoring decisions to help you write Skills that Claude can discover and use effectively.

For conceptual background on how Skills work, see the [Skills overview](/docs/en/agents-and-tools/agent-skills/overview).

## Core principles

### Concise is key

The [context window](/docs/en/build-with-claude/context-windows) is a public good. Your Skill shares the context window with everything else Claude needs to know, including:

* The system prompt
* Conversation history
* Other Skills' metadata
* Your actual request

Not every token in your Skill has an immediate cost. At startup, only the metadata (name and description) from all Skills is pre-loaded. Claude reads SKILL.md only when the Skill becomes relevant, and reads additional files only as needed. However, being concise in SKILL.md still matters: once Claude loads it, every token competes with conversation history and other context.

**Default assumption:** Claude is already very smart

Only add context Claude doesn't already have. Challenge each piece of information:

* "Does Claude really need this explanation?"
* "Can I assume Claude knows this?"
* "Does this paragraph justify its token cost?"

**Good example: Concise** (approximately 50 tokens):

````markdown
## Extract PDF text

Use pdfplumber for text extraction:

```python
import pdfplumber

with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```
````

**Bad example: Too verbose** (approximately 150 tokens):

```markdown
## Extract PDF text

PDF (Portable Document Format) files are a common file format that contains
text, images, and other content. To extract text from a PDF, you'll need to
use a library. There are many libraries available for PDF processing, but
pdfplumber is recommended because it's easy to use and handles most cases well.
First, you'll need to install it using pip. Then you can use the code below...
```

The concise version assumes Claude knows what PDFs are and how libraries work.

### Set appropriate degrees of freedom

Match the level of specificity to the task's fragility and variability.

**High freedom** (text-based instructions):

Use when:

* Multiple approaches are valid
* Decisions depend on context
* Heuristics guide the approach

Example:

```markdown
## Code review process

1. Analyze the code structure and organization
2. Check for potential bugs or edge cases
3. Suggest improvements for readability and maintainability
4. Verify adherence to project conventions
```

**Medium freedom** (pseudocode or scripts with parameters):

Use when:

* A preferred pattern exists
* Some variation is acceptable
* Configuration affects behavior

Example:

````markdown
## Generate report

Use this template and customize as needed:

```python
def generate_report(data, format="markdown", include_charts=True):
    # Process data
    # Generate output in specified format
    # Optionally include visualizations
```
````

**Low freedom** (specific scripts, few or no parameters):

Use when:

* Operations are fragile and error-prone
* Consistency is critical
* A specific sequence must be followed

Example:

````markdown
## Database migration

Run exactly this script:

```bash
python scripts/migrate.py --verify --backup
```

Do not modify the command or add additional flags.
````

**Analogy:** Think of Claude as a robot exploring a path:

* **Narrow bridge with cliffs on both sides:** There's only one safe way forward. Provide specific guardrails and exact instructions (low freedom). Example: database migrations that must run in exact sequence.
* **Open field with no hazards:** Many paths lead to success. Give general direction and trust Claude to find the best route (high freedom). Example: code reviews where context determines the best approach.

### Test with all models you plan to use

Skills act as additions to models, so effectiveness depends on the underlying model. Test your Skill with all the models you plan to use it with.

**Testing considerations by model:**

* **Claude Haiku** (fast, economical): Does the Skill provide enough guidance?
* **Claude Sonnet** (balanced): Is the Skill clear and efficient?
* **Claude Opus** (powerful reasoning): Does the Skill avoid over-explaining?

What works perfectly for Opus might need more detail for Haiku. If you plan to use your Skill across multiple models, aim for instructions that work well with all of them.

## Skill structure

<Note>
  **YAML Frontmatter:** The SKILL.md frontmatter requires two fields:

  `name`:

  * Maximum 64 characters
  * Must contain only lowercase letters, numbers, and hyphens
  * Cannot contain XML tags
  * Cannot contain reserved words: "anthropic", "claude"

  `description`:

  * Must be non-empty
  * Maximum 1024 characters
  * Cannot contain XML tags
  * Should describe what the Skill does and when to use it

  For complete Skill structure details, see the [Skills overview](/docs/en/agents-and-tools/agent-skills/overview#skill-structure).
</Note>

### Naming conventions

Use consistent naming patterns to make Skills easier to reference and discuss. Consider using **gerund form** (verb + -ing) for Skill names, as this clearly describes the activity or capability the Skill provides.

Remember that the `name` field must use lowercase letters, numbers, and hyphens only.

**Good naming examples (gerund form):**

* `processing-pdfs`
* `analyzing-spreadsheets`
* `managing-databases`
* `testing-code`
* `writing-documentation`

**Acceptable alternatives:**

* Noun phrases: `pdf-processing`, `spreadsheet-analysis`
* Action-oriented: `process-pdfs`, `analyze-spreadsheets`

**Avoid:**

* Vague names: `helper`, `utils`, `tools`
* Overly generic: `documents`, `data`, `files`
* Reserved words: `anthropic-helper`, `claude-tools`
* Inconsistent patterns within your skill collection

Consistent naming makes it easier to:

* Reference Skills in documentation and conversations
* Understand what a Skill does at a glance
* Organize and search through multiple Skills
* Maintain a professional, cohesive skill library

### Writing effective descriptions

The `description` field enables Skill discovery and should include both what the Skill does and when to use it.

<Warning>
  **Always write in third person**. The description is injected into the system prompt, and inconsistent point-of-view can cause discovery problems.

  * **Good:** "Processes Excel files and generates reports"
  * **Avoid:** "I can help you process Excel files"
  * **Avoid:** "You can use this to process Excel files"
</Warning>

**Be specific and include key terms**. Include both what the Skill does and specific triggers/contexts for when to use it.

Each Skill has exactly one description field. The description is critical for skill selection: Claude uses it to choose the right Skill from potentially 100+ available Skills. Your description must provide enough detail for Claude to know when to select this Skill, while the rest of SKILL.md provides the implementation details.

Effective examples:

**PDF Processing skill:**

```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

**Excel Analysis skill:**

```yaml
description: Analyze Excel spreadsheets, create pivot tables, generate charts. Use when analyzing Excel files, spreadsheets, tabular data, or .xlsx files.
```

**Git Commit Helper skill:**

```yaml
description: Generate descriptive commit messages by analyzing git diffs. Use when the user asks for help writing commit messages or reviewing staged changes.
```

Avoid vague descriptions like these:

```yaml
description: Helps with documents
```

```yaml
description: Processes data
```

```yaml
description: Does stuff with files
```

### Progressive disclosure patterns

SKILL.md serves as an overview that points Claude to detailed materials as needed, like a table of contents in an onboarding guide. For an explanation of how progressive disclosure works, see [How Skills work](/docs/en/agents-and-tools/agent-skills/overview#how-skills-work) in the overview.

**Practical guidance:**

* Keep SKILL.md body under 500 lines for optimal performance
* Split content into separate files when approaching this limit
* Use the patterns below to organize instructions, code, and resources effectively

#### Visual overview: From simple to complex

A basic Skill starts with just a SKILL.md file containing metadata and instructions:

![Simple SKILL.md file showing YAML frontmatter and markdown body](/docs/images/agent-skills-simple-file.png)

As your Skill grows, you can bundle additional content that Claude loads only when needed:

![Bundling additional reference files like reference.md and forms.md.](/docs/images/agent-skills-bundling-content.png)

The complete Skill directory structure might look like this:

```text
pdf/
├── SKILL.md              # Main instructions (loaded when triggered)
├── FORMS.md              # Form-filling guide (loaded as needed)
├── reference.md          # API reference (loaded as needed)
├── examples.md           # Usage examples (loaded as needed)
└── scripts/
    ├── analyze_form.py   # Utility script (executed, not loaded)
    ├── fill_form.py      # Form filling script
    └── validate.py       # Validation script
```

#### Pattern 1: High-level guide with references

````markdown
---
name: pdf-processing
description: Extracts text and tables from PDF files, fills forms, and merges documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---

# PDF Processing

## Quick start

Extract text with pdfplumber:
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

## Advanced features

**Form filling**: See [FORMS.md](FORMS.md) for complete guide
**API reference**: See [REFERENCE.md](REFERENCE.md) for all methods
**Examples**: See [EXAMPLES.md](EXAMPLES.md) for common patterns
````

Claude loads FORMS.md, REFERENCE.md, or EXAMPLES.md only when needed.

#### Pattern 2: Domain-specific organization

For Skills with multiple domains, organize content by domain to avoid loading irrelevant context. When a user asks about sales metrics, Claude only needs to read sales-related schemas, not finance or marketing data. This keeps token usage low and context focused.

```text
bigquery-skill/
├── SKILL.md (overview and navigation)
└── reference/
    ├── finance.md (revenue, billing metrics)
    ├── sales.md (opportunities, pipeline)
    ├── product.md (API usage, features)
    └── marketing.md (campaigns, attribution)
```

````markdown SKILL.md
# BigQuery Data Analysis

## Available datasets

**Finance**: Revenue, ARR, billing → See [reference/finance.md](reference/finance.md)
**Sales**: Opportunities, pipeline, accounts → See [reference/sales.md](reference/sales.md)
**Product**: API usage, features, adoption → See [reference/product.md](reference/product.md)
**Marketing**: Campaigns, attribution, email → See [reference/marketing.md](reference/marketing.md)

## Quick search

Find specific metrics using grep:

```bash
grep -i "revenue" reference/finance.md
grep -i "pipeline" reference/sales.md
grep -i "api usage" reference/product.md
```
````

#### Pattern 3: Conditional details

Show basic content, link to advanced content:

```markdown
# DOCX Processing

## Creating documents

Use docx-js for new documents. See [DOCX-JS.md](DOCX-JS.md).

## Editing documents

For simple edits, modify the XML directly.

**For tracked changes**: See [REDLINING.md](REDLINING.md)
**For OOXML details**: See [OOXML.md](OOXML.md)
```

Claude reads REDLINING.md or OOXML.md only when the user needs those features.

### Avoid deeply nested references

Claude may partially read files when they're referenced from other referenced files. When encountering nested references, Claude might use commands like `head -100` to preview content rather than reading entire files, resulting in incomplete information.

**Keep references one level deep from SKILL.md**. All reference files should link directly from SKILL.md to ensure Claude reads complete files when needed.

**Bad example: Too deep**:

```markdown
# SKILL.md
See [advanced.md](advanced.md)...

# advanced.md
See [details.md](details.md)...

# details.md
Here's the actual information...
```

**Good example: One level deep**:

```markdown
# SKILL.md

**Basic usage**: [instructions in SKILL.md]
**Advanced features**: See [advanced.md](advanced.md)
**API reference**: See [reference.md](reference.md)
**Examples**: See [examples.md](examples.md)
```

### Structure longer reference files with table of contents

For reference files longer than 100 lines, include a table of contents at the top. This ensures Claude can see the full scope of available information even when previewing with partial reads.

**Example:**

```markdown
# API Reference

## Contents
- Authentication and setup
- Core methods (create, read, update, delete)
- Advanced features (batch operations, webhooks)
- Error handling patterns
- Code examples

## Authentication and setup
...

## Core methods
...
```

Claude can then read the complete file or jump to specific sections as needed.

For details on how this filesystem-based architecture enables progressive disclosure, see the [Runtime environment](#runtime-environment) section in the Advanced section below.

## Workflows and feedback loops

### Use workflows for complex tasks

Break complex operations into clear, sequential steps. For particularly complex workflows, provide a checklist that Claude can copy into its response and check off as it progresses.

**Example 1: Research synthesis workflow** (for Skills without code):

````markdown
## Research synthesis workflow

Copy this checklist and track your progress:

```
Research Progress:
- [ ] Step 1: Read all source documents
- [ ] Step 2: Identify key themes
- [ ] Step 3: Cross-reference claims
- [ ] Step 4: Create structured summary
- [ ] Step 5: Verify citations
```

**Step 1: Read all source documents**

Review each document in the `sources/` directory. Note the main arguments and supporting evidence.

**Step 2: Identify key themes**

Look for patterns across sources. What themes appear repeatedly? Where do sources agree or disagree?

**Step 3: Cross-reference claims**

For each major claim, verify it appears in the source material. Note which source supports each point.

**Step 4: Create structured summary**

Organize findings by theme. Include:
- Main claim
- Supporting evidence from sources
- Conflicting viewpoints (if any)

**Step 5: Verify citations**

Check that every claim references the correct source document. If citations are incomplete, return to Step 3.
````

This example shows how workflows apply to analysis tasks that don't require code. The checklist pattern works for any complex, multi-step process.

**Example 2: PDF form filling workflow** (for Skills with code):

````markdown
## PDF form filling workflow

Copy this checklist and check off items as you complete them:

```
Task Progress:
- [ ] Step 1: Analyze the form (run analyze_form.py)
- [ ] Step 2: Create field mapping (edit fields.json)
- [ ] Step 3: Validate mapping (run validate_fields.py)
- [ ] Step 4: Fill the form (run fill_form.py)
- [ ] Step 5: Verify output (run verify_output.py)
```

**Step 1: Analyze the form**

Run: `python scripts/analyze_form.py input.pdf`

This extracts form fields and their locations, saving to `fields.json`.

**Step 2: Create field mapping**

Edit `fields.json` to add values for each field.

**Step 3: Validate mapping**

Run: `python scripts/validate_fields.py fields.json`

Fix any validation errors before continuing.

**Step 4: Fill the form**

Run: `python scripts/fill_form.py input.pdf fields.json output.pdf`

**Step 5: Verify output**

Run: `python scripts/verify_output.py output.pdf`

If verification fails, return to Step 2.
````

Clear steps prevent Claude from skipping critical validation. The checklist helps both Claude and you track progress through multi-step workflows.

### Implement feedback loops

**Common pattern:** Run validator → fix errors → repeat

This pattern greatly improves output quality.

**Example 1: Style guide compliance** (for Skills without code):

```markdown
## Content review process

1. Draft your content following the guidelines in STYLE_GUIDE.md
2. Review against the checklist:
   - Check terminology consistency
   - Verify examples follow the standard format
   - Confirm all required sections are present
3. If issues found:
   - Note each issue with specific section reference
   - Revise the content
   - Review the checklist again
4. Only proceed when all requirements are met
5. Finalize and save the document
```

This shows the validation loop pattern using reference documents instead of scripts. The "validator" is STYLE\_GUIDE.md, and Claude performs the check by reading and comparing.

**Example 2: Document editing process** (for Skills with code):

```markdown
## Document editing process

1. Make your edits to `word/document.xml`
2. **Validate immediately**: `python ooxml/scripts/validate.py unpacked_dir/`
3. If validation fails:
   - Review the error message carefully
   - Fix the issues in the XML
   - Run validation again
4. **Only proceed when validation passes**
5. Rebuild: `python ooxml/scripts/pack.py unpacked_dir/ output.docx`
6. Test the output document
```

The validation loop catches errors early.

## Content guidelines

### Avoid time-sensitive information

Don't include information that will become outdated:

**Bad example: Time-sensitive** (will become wrong):

```markdown
If you're doing this before August 2025, use the old API.
After August 2025, use the new API.
```

**Good example** (use "old patterns" section):

```markdown
## Current method

Use the v2 API endpoint: `api.example.com/v2/messages`

## Old patterns

<details>
<summary>Legacy v1 API (deprecated 2025-08)</summary>

The v1 API used: `api.example.com/v1/messages`

This endpoint is no longer supported.
</details>
```

The old patterns section provides historical context without cluttering the main content.

### Use consistent terminology

Choose one term and use it throughout the Skill:

**Good - Consistent:**

* Always "API endpoint"
* Always "field"
* Always "extract"

**Bad - Inconsistent:**

* Mix "API endpoint", "URL", "API route", "path"
* Mix "field", "box", "element", "control"
* Mix "extract", "pull", "get", "retrieve"

Consistency helps Claude understand and follow instructions.

## Common patterns

### Template pattern

Provide templates for output format. Match the level of strictness to your needs.

**For strict requirements** (like API responses or data formats):

````markdown
## Report structure

ALWAYS use this exact template structure:

```markdown
# [Analysis Title]

## Executive summary
[One-paragraph overview of key findings]

## Key findings
- Finding 1 with supporting data
- Finding 2 with supporting data
- Finding 3 with supporting data

## Recommendations
1. Specific actionable recommendation
2. Specific actionable recommendation
```
````

**For flexible guidance** (when adaptation is useful):

````markdown
## Report structure

Here is a sensible default format, but use your best judgment based on the analysis:

```markdown
# [Analysis Title]

## Executive summary
[Overview]

## Key findings
[Adapt sections based on what you discover]

## Recommendations
[Tailor to the specific context]
```

Adjust sections as needed for the specific analysis type.
````

### Examples pattern

For Skills where output quality depends on seeing examples, provide input/output pairs just like in regular prompting:

````markdown
## Commit message format

Generate commit messag