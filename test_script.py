import os
import tempfile
import time
import scaledown as sd
# Optional Optimizers (Lazy Loaded)
from scaledown.optimizer import HasteOptimizer, SemanticOptimizer
from scaledown.exceptions import AuthenticationError, APIError


API_KEY = os.environ.get("SCALEDOWN_API_KEY")
sd.set_api_key("IEUaw02XYd8ElTDoRZ6Gx6ORRASCx1EP1L3vZq9z")

if API_KEY == "IEUaw02XYd8ElTDoRZ6Gx6ORRASCx1EP1L3vZq9z":
    print("Warning: Using placeholder API key. API calls will fail.")
    print("Export your key: export SCALEDOWN_API_KEY='sk_...'\n")

TEST_CODE = """
Lionel Andrés Messi (Spanish pronunciation: [ljo'nel an'dɾes 'mesi]; born 24 June 1987), also known as Leo Messi, is an Argentine professional footballer who plays as a forward for Ligue 1 club Paris Saint-Germain and captains the Argentina national team. Widely regarded as one of the greatest players of all time, Messi has won a record seven Ballon d'Or awards,[note 2] a record six European Golden Shoes, and in 2020 was named to the Ballon d'Or Dream Team. Until leaving the club in 2021, he had spent his entire professional career with Barcelona, where he won a club-record 35 trophies, including 10 La Liga titles, seven Copa del Rey titles and four UEFA Champions Leagues. With his country, he won the 2021 Copa América and the 2022 FIFA World Cup. A prolific goalscorer and creative playmaker, Messi holds the records for most goals in La Liga (474), most hat-tricks in La Liga (36) and the UEFA Champions League (8), and most assists in La Liga (192) and the Copa América (17). He has also the most international goals by a South American male (98). Messi has scored over 795 senior career goals for club and country, and has the most goals by a player for a single club (672).
Born and raised in central Argentina, Messi relocated to Spain at the age of 13 to join Barcelona, for whom he made his competitive debut aged 17 in October 2004. He established himself as an integral player for the club within the next three years, and in his first uninterrupted season in 2008-09 he helped Barcelona achieve the first treble in Spanish football; that year, aged 22, Messi won his first Ballon d'Or. Three successful seasons followed, with Messi winning four consecutive Ballons d'Or, making him the first player to win the award four times. During the 2011-12 season, he set the La Liga and European records for most goals scored in a single season, while establishing himself as Barcelona's all-time top scorer. The following two seasons, Messi finished second for the Ballon d'Or behind Cristiano Ronaldo (his perceived career rival), before regaining his best form during the 2014-15 campaign, becoming the all-time top scorer in La Liga and leading Barcelona to a historic second treble, after which he was awarded a fifth Ballon d'Or in 2015. Messi assumed captaincy of Barcelona in 2018, and in 2019 he won a record sixth Ballon d'Or. Out of contract, he signed for Paris Saint-Germain in August 2021.
An Argentine international, Messi holds the national record for appearances and is also the country's all-time leading goalscorer. At youth level, he won the 2005 FIFA World Youth Championship, finishing the tournament with both the Golden Ball and Golden Shoe, and an Olympic gold medal at the 2008 Summer Olympics. His style of play as a diminutive, left-footed dribbler drew comparisons with his compatriot Diego Maradona, who described Messi as his successor. After his senior debut in August 2005, Messi became the youngest Argentine to play and score in a FIFA World Cup in 2006, and reached the final of the 2007 Copa América, where he was named young player of the tournament. As the squad's captain from August 2011, he led Argentina to three consecutive finals: the 2014 FIFA World Cup, for which he won the Golden Ball, and the 2015 and 2016 Copa América, winning the Golden Ball in the 2015 edition. After announcing his international retirement in 2016, he reversed his decision and led his country to qualification for the 2018 FIFA World Cup, a third-place finish at the 2019 Copa América, and victory in the 2021 Copa América, while winning the Golden Ball and Golden Boot for the latter. This achievement would see him receive a record seventh Ballon d'Or in 2021. In 2022, he captained his country to win the 2022 FIFA World Cup, for which he won the Golden Ball for a record second time, and broke the record for most appearances in World Cup tournaments with 26 matches played.
Messi has endorsed sportswear company Adidas since 2006. According to France Football, he was the world's highest-paid footballer for five years out of six between 2009 and 2014, and was ranked the world's highest-paid athlete by Forbes in 2019 and 2022. Messi was among Time's 100 most influential people in the world in 2011 and 2012. In February 2020, he was awarded the Laureus World Sportsman of the Year, thus becoming the first footballer and the first team sport athlete to win the award. Later that year, Messi became the second footballer and second team-sport athlete to surpass $1 billion in career earnings.
"""

def print_header(title):
    print("\n" + "-" * 60)
    print(f"{title}")
    print("-" * 60)

def print_step_details(step_name, content, metrics):
    print(f"\n[{step_name}]")
    
    # Handle different metric structures safely
    in_tok = metrics.get('original_tokens', metrics.get('input_tokens', '?'))
    out_tok = metrics.get('optimized_tokens', metrics.get('compressed_tokens', metrics.get('output_tokens', '?')))
    
    print(f"Tokens: {in_tok} -> {out_tok}")
    
    if 'latency_ms' in metrics:
        print(f"Latency: {metrics['latency_ms']:.0f}ms")
    
    preview = content.strip()[:150].replace('\n', ' ')
    print(f"Preview: {preview}{'...' if len(content) > 150 else ''}")

# main test logic
with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
    f.write(TEST_CODE)
    file_path_arg = f.name

try:
    print_header("Component tests")

    # # 1. test semantic
    # print("\nTesting SemanticOptimizer...", end=" ")
    # try:
    #     opt = SemanticOptimizer(top_k=1)
    #     res = opt.optimize(context=TEST_CODE, query="DataProcessor", file_path=file_path_arg)
    #     print("Passed")
        
    #     metrics_dict = res.metrics.__dict__ if hasattr(res.metrics, '__dict__') else {}
    #     print_step_details("Semantic output", res.content, metrics_dict)
    # except ImportError:
    #     print("Skipped (missing dependencies)")
    # except Exception as e:
    #     print(f"Failed: {e}")

    # # 2. test haste
    # print("\nTesting HasteOptimizer...", end=" ")
    # try:
    #     opt = HasteOptimizer(top_k=2)
    #     res = opt.optimize(context=TEST_CODE, query="calculate_average", file_path=file_path_arg, target_model="gpt-4o")
    #     print("Passed")
        
    #     metrics_dict = res.metrics.__dict__ if hasattr(res.metrics, '__dict__') else {}
    #     print_step_details("Haste output", res.content, metrics_dict)
    # except ImportError:
    #      print("Skipped (missing dependencies)")
    # except Exception as e:
    #     print(f"Failed: {e}")

    # # 3. test compressor
    # print("\nTesting ScaleDownCompressor...", end=" ")
    try:
        comp = sd.ScaleDownCompressor(target_model="gpt-4o")
        res = comp.compress(
            context=TEST_CODE,
            prompt="Ultra-compress to ≤400 characters. Prioritize numeric and named-entity retention only. Convert all facts to compact symbolic notation. Remove syntax, grammar, and readability constraints. No sentences. No filler. Dense fact encoding only. Output raw compressed block."
        )
        print("Passed")
        
        metrics_dict = {
            "original_tokens": res.tokens[0], 
            "compressed_tokens": res.tokens[1],
            "latency_ms": 0 
        }
        print_step_details("Compressor output", res.content, metrics_dict)
        if len(res.content) < 226:
            print("Compressed text too shor, using original text instead")
            res.content = TEST_CODE
    except Exception as e:
        print(f"Failed: {e}")

    # 4. full pipeline
    print_header("Pipeline integration")
    
    steps = []
    # try:
    #     steps.append(('haste', HasteOptimizer(top_k=5)))
    # except ImportError: pass
    
    # try:
    #     steps.append(('semantic', SemanticOptimizer(top_k=1)))
    # except ImportError: pass
        
    steps.append(('compressor', sd.ScaleDownCompressor(target_model="gpt-4o")))

    pipeline = sd.Pipeline(steps)
    print(f"Configuration: {[s[0] for s in steps]}")

    result = pipeline.run(
        context=TEST_CODE,
        query="logic for processing",
        file_path=file_path_arg,
        prompt="Ultra-compress to ≤400 characters. Prioritize numeric and named-entity retention only. Convert all facts to compact symbolic notation. Remove syntax, grammar, and readability constraints. No sentences. No filler. Dense fact encoding only. Output raw compressed block."
    )

    print(result.final_content)

    if len(result.final_content) < 226:
        print("Pipeline output too short, using original text instead")
        result.final_content = TEST_CODE
    print("Final content length:", len(result.final_content))
    
    print("Pipeline finished successfully")
    
    print("\n--- Trace ---")
    for i, step in enumerate(result.history):
        print(f"\nStep {i+1}: {step.step_name}")
        print(f"  Latency: {step.latency_ms:.0f}ms")
        print(f"  Tokens:  {step.input_tokens} -> {step.output_tokens}")
        

    print_header("Summary")
    print(f"Original size: {len(TEST_CODE)} chars")
    print(f"Final size:    {len(result.final_content)} chars")
    print(f"Savings:       {result.savings_percent:.1f}%")

except Exception as e:
    print(f"\nError: {e}")

finally:
    if os.path.exists(file_path_arg):
        os.unlink(file_path_arg)
